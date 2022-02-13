import os
import sys

from . import dependencies, install, remove, showlist, updates, custom


def runArchInstaller():
    all_args = sys.argv[1:]

    # Install program
    if all_args[0].strip() == "install":
        install.installPackage(args=all_args[1:])

    # Force Install (install without confirmation)
    elif (all_args[0].strip() in ("installf", "finstall", "force-install",
                                  "forceinstall", "installforce",
                                  "install-force")):
        install.installPackageForce(args=all_args[1:])

    # Remove program
    elif (all_args[0].strip() in ("remove", "uninstall")):
        remove.removePackage(args=all_args[1:])

    # Remove Program with dependencies
    elif (all_args[0].strip() in ("allremove", "removeall", "all-remove",
                                  "remove-all", "removea")):
        remove.removePackageWithDependencies(args=all_args[1:])
