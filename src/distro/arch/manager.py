import os
import sys

from . import dependencies, install, remove, showlist, updates


def runArchInstaller():
    all_args = sys.argv[1:]
    if all_args[0].strip() == "install":
        install.installPackage(args=all_args[1:])
