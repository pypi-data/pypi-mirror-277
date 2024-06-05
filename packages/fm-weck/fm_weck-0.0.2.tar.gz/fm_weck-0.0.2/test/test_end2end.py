# This file is part of fm-weck: executing fm-tools in containerized environments.
# https://gitlab.com/sosy-lab/software/fm-weck
#
# SPDX-FileCopyrightText: 2024 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from fm_weck.cli import cli

YAML_REMOTE = """
name: Goblint
input_languages:
  - C
project_url: https://goblint.in.tum.de/
repository_url: https://github.com/goblint/analyzer
spdx_license_identifier: MIT
benchexec_toolinfo_module: "https://gitlab.com/sosy-lab/software/benchexec/-/raw/main/benchexec/tools/goblint.py"
fmtools_format_version: "2.0"
fmtools_entry_maintainers:
  - sim642

maintainers:
  - name: Simmo Saan
    institution: University of Tartu
    country: Estonia
    url: https://sim642.eu/
  - name: Michael Schwarz
    institution: Technische Universität München
    country: Germany
    url: https://www.cs.cit.tum.de/en/pl/personen/michael-schwarz/

versions:
  - version: "svcomp24"
    doi: 10.5281/zenodo.10202867
    benchexec_toolinfo_options: ["--conf", "conf/svcomp24.json"]
    required_ubuntu_packages: []

"""
HERE = Path(__file__).parent


def test_list(fs, capsys):
    fs.create_file(HERE.parent / "src" / "fm_weck" / "resources" / "fm_tools" / "cpachecker.yaml")
    fs.create_file(HERE.parent / "src" / "fm_weck" / "resources" / "properties" / "unreach-call.prp")
    cli(["--list"])

    captured = capsys.readouterr()

    assert "- cpachecker" in captured.out
    assert "- unreach-call" in captured.out
