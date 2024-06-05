# This file is part of fm-weck: executing fm-tools in containerized environments.
# https://gitlab.com/sosy-lab/software/fm-weck
#
# SPDX-FileCopyrightText: 2024 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import logging
import shutil
from functools import cache
from pathlib import Path
from typing import Optional

from fm_weck.config import Config, parse_fm_data

from .engine import Engine
from .resources import iter_fm_data, iter_properties


@cache
def fm_tools_choice_map():
    ignore = {
        "schema.yml",
    }

    actors = {actor_def.stem: actor_def for actor_def in iter_fm_data() if (actor_def.name not in ignore)}

    return actors


@cache
def property_choice_map():
    return {spec_path.stem: spec_path for spec_path in iter_properties() if spec_path.suffix != ".license"}


def list_known_tools():
    return fm_tools_choice_map().keys()


def list_known_properties():
    return property_choice_map().keys()


def resolve_tool(tool_name: str) -> Path:
    if (as_path := Path(tool_name)).exists() and as_path.is_file():
        return as_path

    return fm_tools_choice_map()[tool_name]


def resolve_property(prop_name: str) -> Path:
    if (as_path := Path(prop_name)).exists() and as_path.is_file():
        return as_path

    return property_choice_map()[prop_name]


def serve(
    fm_tool: str,
    version: Optional[str],
    configuration: Config,
    prop: Optional[str],
    program_files: list[Path],
    additional_args: list[str],
    skip_download: bool = False,
):
    try:
        tool_path = resolve_tool(fm_tool)
    except KeyError:
        logging.error("Unknown tool %s", fm_tool)
        return 1

    property_path = None
    if prop is not None:
        try:
            # the source path might not be mounted in the contianer, so we
            # copy the property to the weck_cache which should be mounted
            source_property_path = resolve_property(prop)
            property_path = configuration.get_shelve_path_for_property(source_property_path)
            shutil.copyfile(source_property_path, property_path)
        except KeyError:
            logging.error("Unknown property %s", prop)
            return 1

    fm_data = parse_fm_data(tool_path, version)

    engine = Engine.from_config(fm_data, configuration)

    shelve_space = configuration.get_shelve_space_for(fm_data)
    logging.debug("Using shelve space %s", shelve_space)

    if not skip_download:
        fm_data.download_and_install_into(shelve_space)
    fm_data.get_toolinfo_module().make_available()

    command = fm_data.command_line(
        shelve_space,
        input_files=program_files,
        working_dir=engine.get_workdir(),
        property=property_path,
        options=additional_args,
    )

    logging.debug("Assembled command from fm-tools:", command)

    engine.run(*command)
