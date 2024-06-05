# This file is part of fm-weck: executing fm-tools in containerized environments.
# https://gitlab.com/sosy-lab/software/fm-weck
#
# SPDX-FileCopyrightText: 2024 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

import pytest
from fm_weck.config import Config
from fm_weck.engine import Engine


@pytest.fixture
def config():
    """
    Arrange the Config object to a known state before the test.
    """
    config = Config()
    config._config = {
        "logging": {"level": "INFO"},
        "defaults": {"image": "some_image:latest", "cache_location": ".weck_cache"},
        "mount": {"/abs/to/local/path": "/container/path"},
    }
    return config


def test_assemble_command(fs, config):
    fs.create_file("/abs/to/local/path")

    engine = Engine.from_config(config)
    command = engine.assemble_command(("echo", "Hello, World!"))

    expected = [
        "podman",
        "run",
        "--annotation",
        "run.oci.keep_original_groups=1",
        "--security-opt",
        "unmask=/proc/*",
        "--security-opt",
        "seccomp=unconfined",
        "-v",
        "/sys/fs/cgroup:/sys/fs/cgroup",
        "-v",
        f"{Path.cwd().absolute()}:/home/cwd",
        "--workdir",
        "/home/cwd",
        "--rm",
        "-v",
        "/abs/to/local/path:/container/path",
        "some_image:latest",
        "echo",
        "Hello, World!",
    ]

    assert command == expected


@pytest.mark.skip(reason="relative paths from config are in development")
def test_assemble_command_with_mount(fs, config):
    fs.create_file("local/path")
    config._config["mount"] = {"local/path": "/container/path"}

    engine = Engine.from_config(config)
    command = engine.assemble_command(("echo", "Hello, World!"))

    expected = [
        "podman",
        "run",
        "--annotation",
        "run.oci.keep_original_groups=1",
        "--security-opt",
        "unmask=/proc/*",
        "--security-opt",
        "seccomp=unconfined",
        "-v",
        "/sys/fs/cgroup:/sys/fs/cgroup",
        "-v",
        f"{Path.cwd().absolute()}:/home/cwd",
        "--workdir",
        "/home/cwd",
        "--rm",
        "-v",
        f"{Path.cwd().absolute()}/local/path:/container/path",
        "some_image:latest",
        "echo",
        "Hello, World!",
    ]

    assert command == expected
