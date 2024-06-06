# This file is part of fm-weck: executing fm-tools in containerized environments.
# https://gitlab.com/sosy-lab/software/fm-weck
#
# SPDX-FileCopyrightText: 2024 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import argparse
import logging
from functools import cache
from pathlib import Path
from typing import Any, Optional

from fm_weck import Config
from fm_weck.resources import iter_fm_data, iter_properties

from .engine import Engine
from .serve import serve


def parse(raw_args: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="fm-weck")

    parser.add_argument(
        "--config",
        action="store",
        type=Path,
        help="Path to the configuration file.",
        default=None,
    )

    parser.add_argument(
        "--loglevel",
        choices=["debug", "info", "warning", "error", "critical"],
        action="store",
        default=None,
        help="Set the log level.",
    )

    parser.add_argument(
        "fm_data",
        help=(
            "The fm-data file to use."
            "Can be either a path to the fm-too yaml file or the name of the tool. "
            "For a full list of supported names call 'fm-weck serve --list'"
        ),
        nargs="?",
        metavar="fm-data",
    )

    parser.add_argument(
        "-V",
        "--version",
        action="store",
        help="Version within the fm-tools that shall be used",
        required=False,
        default=None,
    )

    parser.add_argument(
        "--list",
        action="store_true",
        help="List all fm-tools that can be called by name.",
        required=False,
        default=False,
    )

    subparsers = parser.add_subparsers()
    shell = subparsers.add_parser("shell", help="Enter an interactive shell.")
    run = subparsers.add_parser("run", help="Run a command in the container")
    serve = subparsers.add_parser("serve", help="Serve a tool")

    run.add_argument("command", help="Command to run")
    run.add_argument("args", nargs="*", help="Arguments for the command")

    serve.add_argument(
        "--skip-download",
        action="store_true",
        help="Do not download the fm-tool, even if it is not available in the cache.",
        default=False,
    )

    serve.add_argument(
        "-p",
        "--property",
        "--spec",
        action="store",
        help=(
            "Property to that is forwarded to the fm-tool."
            " Either a path to a property file or a property name from SV-COMP or Test-Comp."
            " Use fm-weck serve --list to see all properties that can be called ba name."
        ),
        required=False,
        default=None,
    )

    serve.add_argument(
        "--file",
        "--program",
        "--programs",
        "--files",
        action="store",
        type=Path,
        help="Programs to pass to the tool",
        nargs="+",
    )

    serve.add_argument("argument_list", metavar="args", nargs="*", help="Arguments for the fm-tool")

    serve.set_defaults(entry=main_serve)
    shell.set_defaults(entry=main_shell)
    run.set_defaults(entry=main_run)
    return parser, parser.parse_args(raw_args)


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


def set_log_level(loglevel: Optional[str], config: dict[str, Any]):
    level = "WARNING"
    level = loglevel.upper() if loglevel else config.get("logging", {}).get("level", level)
    logging.basicConfig(level=level)


def main_serve(args: argparse.Namespace):
    if not args.fm_data:
        logging.error("No fm-tool given. Aborting...")
        return 1
    try:
        fm_data = resolve_tool(args.fm_data)
    except KeyError:
        logging.error("Unknown tool %s", fm_data)
        return 1

    try:
        property_path = resolve_property(args.property) if args.property else None
    except KeyError:
        logging.error("Unknown property %s", args.property)
        return 1

    serve(
        fm_tool=fm_data,
        version=args.version,
        configuration=Config(),
        prop=property_path,
        program_files=args.file,
        additional_args=args.argument_list,
        skip_download=args.skip_download,
    )


def main_run(args: argparse.Namespace):
    if not args.fm_data:
        engine = Engine.from_config(Config())
    else:
        try:
            fm_data = resolve_tool(args.fm_data)
        except KeyError:
            logging.error("Unknown tool %s", fm_data)
            return 1
        engine = Engine.from_config(fm_data, args.version, Config())
    engine.run(args.command, *args.args)


def main_shell(args: argparse.Namespace):
    if not args.fm_data:
        engine = Engine.from_config(Config())
    else:
        try:
            fm_data = resolve_tool(args.fm_data)
        except KeyError:
            logging.error("Unknown tool %s", fm_data)
            return 1
        engine = Engine.from_config(fm_data, args.version, Config())
    engine.interactive = True
    engine.run("/bin/bash")


def cli(raw_args: list[str]):
    parser, args = parse(raw_args)
    configuration = Config().load(args.config)
    set_log_level(args.loglevel, configuration)

    if args.list:
        print("List of fm-tools callable by name:")
        for tool in sorted(list_known_tools()):
            print(f"  - {tool}")
        print("\nList of properties callable by name:")
        for prop in sorted(list_known_properties()):
            print(f"  - {prop}")
        return

    if not hasattr(args, "entry"):
        parser.print_help()
        return

    args.entry(args)
