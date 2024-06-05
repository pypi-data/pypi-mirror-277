# The MIT License (MIT)
#
# Copyright (c) 2019 Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
A command-line tool to switch between several Git profiles. Switching to a
profile will load configuration options from a Git configuration file and
write them to the current repository.
"""

from __future__ import annotations
import argparse
import base64
import configparser
import enum
import json
import os
import subprocess
import sys
from tempfile import TemporaryDirectory
from pathlib import Path
from shlex import quote
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from databind.json import load as from_json, dump as to_json

from ._vendor.gitconfigparser import GitConfigParser

__author__ = "Niklas Rosenstein <rosensteinniklas@gmail.com>"
__version__ = "1.1.3"


def git(*args: str) -> str:
    command = "git " + " ".join(map(quote, args))
    return subprocess.check_output(command, shell=True).decode().strip()


def find_git_dir() -> str | None:
    directory = os.getcwd()
    prev = None
    while True:
        path = os.path.join(directory, ".git")
        if os.path.exists(path):
            if os.path.isfile(path):
                with open(path) as fp:
                    for line in fp:
                        if line.startswith("gitdir:"):
                            return line.replace("gitdir:", "").strip()
                raise RuntimeError('unable to find gitdir in "{}"'.format(path))
            return path
        directory = os.path.dirname(directory)
        if directory == prev:
            return None
        prev = directory
    assert False


@dataclass
class Change:
    type: ChangeType
    section: str
    key: str | None
    value: str | None


class ChangeType(enum.Enum):
    NEW = enum.auto()
    SET = enum.auto()
    DEL = enum.auto()


@dataclass
class Changeset:
    changes: list[Change] = field(default_factory=list)

    @classmethod
    def from_b64(cls, data: bytes) -> "Changeset":
        return Changeset(from_json(json.loads(base64.b64decode(data).decode("utf8")), list[Change]))

    def to_b64(self) -> bytes:
        return base64.b64encode(json.dumps(to_json(self.changes, list[Change])).encode("utf8"))

    def revert(self, config: configparser.RawConfigParser) -> None:
        for change in reversed(self.changes):
            if change.type == ChangeType.NEW:
                if change.key is None:
                    config.remove_section(change.section)
                else:
                    config.remove_option(change.section, change.key)
            elif change.type == ChangeType.SET or change.type == ChangeType.DEL:
                assert change.section and change.key and change.value, change
                config.set(change.section, change.key, change.value)
            else:
                raise RuntimeError("unexpected Change.type: {!r}".format(change))

    def set(self, config: configparser.RawConfigParser, section: str, key: str, value: str) -> None:
        if not config.has_section(section):
            config.add_section(section)
            self.changes.append(Change(ChangeType.NEW, section, None, None))
        if not config.has_option(section, key):
            self.changes.append(Change(ChangeType.NEW, section, key, None))
        else:
            self.changes.append(Change(ChangeType.SET, section, key, config.get(section, key)))
        config.set(section, key, value)


if TYPE_CHECKING:

    class _MergeReadConfigBase(GitConfigParser): ...
else:

    class _MergeReadConfigBase: ...


class MergeReadConfig(_MergeReadConfigBase):
    def __init__(self, configs: list[GitConfigParser]):
        self.configs = configs

    def __getattr__(self, name: str) -> Any:
        return getattr(self.configs[0], name)

    def get_value(self, section: str, option: str, default: str | None = None) -> str:
        for cfg in self.configs:
            try:
                return cfg.get(section, option)
            except configparser.NoOptionError:
                pass
        if default is not None:
            return default
        raise configparser.NoOptionError(option, section)


def main(argv: list[str] | None = None, prog: str | None = None) -> int:
    parser = argparse.ArgumentParser(prog=prog)
    parser.add_argument("profile", nargs="?", help="The name of the profile to use.")
    parser.add_argument("-d", "--diff", action="store_true", help="Print the config diff.")
    args = parser.parse_args(argv)

    global_config = GitConfigParser(os.path.expanduser("~/.gitconfig"))  # type: ignore[no-untyped-call]
    profiles = set(x.split(".")[0] for x in global_config.sections() if "." in x and " " not in x)
    profiles.add("default")

    git_dir = find_git_dir()
    if not git_dir:
        print("fatal: GIT_DIR not found", file=sys.stderr)
        return 1

    local_config_fn = os.path.join(git_dir, "config")
    assert os.path.isfile(local_config_fn), local_config_fn
    local_config = GitConfigParser(local_config_fn, read_only=False)  # type: ignore[no-untyped-call]
    current_profile = local_config.get_value("profile", "current", "default")  # type: ignore[no-untyped-call]
    current_config_text = Path(local_config_fn).read_text()

    if not args.profile:
        for x in sorted(profiles, key=lambda x: x.lower()):
            print("*" if x == current_profile else " ", x)
        return 0
    else:
        if args.profile not in profiles:
            print('fatal: no such profile: "{}"'.format(args.profile), file=sys.stderr)
            return 1

        config = MergeReadConfig([local_config, global_config])
        changeset: str = local_config.get_value("profile", "changeset", "")  # type: ignore[no-untyped-call]
        if changeset:
            changes = Changeset.from_b64(changeset.encode("ascii"))
            changes.revert(config)

        if args.profile != "default":
            changes = Changeset()
            for section in global_config.sections():
                if section.startswith(args.profile + "."):
                    key = section.split(".", 1)[1]
                    for opt in global_config.options(section):
                        changes.set(config, key, opt, global_config.get_value(section, opt))  # type: ignore
            changes.set(local_config, "profile", "current", args.profile)
            changes.set(local_config, "profile", "changeset", changes.to_b64().decode("ascii"))

        local_config.write()
        del local_config

        if args.diff and Path(local_config_fn).read_text() != current_config_text:
            with TemporaryDirectory() as tmpdir:
                tmpfile = os.path.join(tmpdir, "_old.ini")
                with open(tmpfile, "w") as fp:
                    fp.write(current_config_text)
                    fp.close()
                print()
                subprocess.call(["git", "diff", "--no-index", tmpfile, local_config_fn])
                print()

        print('Switched to profile "{}".'.format(args.profile))
        return 0


if __name__ == "__main__":
    sys.exit(main())
