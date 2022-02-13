import os
import sys

# import src.utils.db as db
# import src.utils.dirs as dirs


def removePackage(args: list = None):
    if args is None:
        sys.exit("[E] Please enter the package names to remove")

    final_command = ""
    for arg in args:
        # to prevent passing the same argument twice
        if str(arg).strip().startswith("-R"):
            continue
        final_command += f"{arg} "

    os.system(f"yay -R {final_command}")


def removePackageWithDependencies(args: list = None):
    if args is None:
        sys.exit("[E] Please enter the package names to remove")

    final_command = ""
    for arg in args:
        # to prevent passing the same argument twice
        if str(arg).strip().startswith("-R"):
            continue
        final_command += f"{arg} "

    os.system(f"yay -Rs {final_command}")
