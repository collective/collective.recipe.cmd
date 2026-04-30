# Copyright (C)2007 Ingeniweb

"""Recipe cmd"""

from pathlib import Path
from subprocess import check_call

import doctest
import sys
import tempfile


def as_bool(value):
    if value.lower() in ("1", "true"):
        return True
    return False


def run_commands(cmds, shell):
    cmds = cmds.strip()
    if not cmds:
        return
    lines = cmds.split("\n")
    lines = [line.strip() for line in lines]
    with tempfile.TemporaryDirectory() as dirname:
        tmpdir = Path(dirname)
        if sys.platform == "win32":
            tmpfile = tmpdir / "run.bat"
            lines.insert(0, "@echo off")
        else:
            tmpfile = tmpdir / "run"
        tmpfile.write_text("\n".join(lines))
        if sys.platform == "win32":
            check_call(str(tmpfile), shell=True)
        else:
            check_call(f"{shell} {tmpfile}", shell=True)


class Cmd:
    """This recipe is used by zc.buildout"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        self.on_install = as_bool(options.get("on_install", "false"))
        self.on_update = as_bool(options.get("on_update", "false"))
        self.shell = options.get("shell", "sh")

    def install(self):
        """installer"""
        if self.on_install:
            self.execute()
        return tuple()

    def update(self):
        """updater"""
        if self.on_update:
            self.execute()
        return tuple()

    def execute(self):
        """run the commands"""
        cmds = self.options.get("cmds", "")
        run_commands(cmds, self.shell)


def uninstallCmd(name, options):
    cmds = options.get("uninstall_cmds", "")
    shell = options.get("shell", "sh")
    run_commands(cmds, shell)


class Python(Cmd):

    def execute(self):
        """run python code"""
        cmds = self.options.get("cmds", "")
        cmds = cmds.strip()

        if not cmds:
            return
        name = self.name
        buildout = self.buildout
        options = self.options
        parser = doctest.DocTestParser()
        parsed = parser.parse(cmds)
        lines = [item.source for item in parsed if isinstance(item, doctest.Example)]
        with tempfile.TemporaryDirectory() as dirname:
            tmpfile = Path(dirname) / "run.py"
            tmpfile.write_text("".join(lines) + "\n")
            code = tmpfile.read_text()
            exec(code, globals(), locals())
