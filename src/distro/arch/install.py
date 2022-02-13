import os
import sys

# import src.utils.db as db
# import src.utils.dirs as dirs


def installPackage(args: list = None):
    if args is None:
        sys.exit("[E] Please enter the package names to install")

    final_command = ""
    for arg in args:
        # to prevent passing the same argument twice
        if str(arg).strip().startswith("-S"):
            continue
        final_command += f"{arg} "

    os.system(f"yay -S {final_command}")


def installPackageForce(args: list = None):
    if args is None:
        sys.exit("[E] Please enter the package names to install")

    final_command = ""
    for arg in args:
        # to prevent passing the same arguments twice
        if str(arg).strip().startswith("-S"):
            continue
        if str(arg).strip().startswith("--noconfirm"):
            continue
        final_command += f"{arg} "

    os.system(f"yay -S {final_command} --noconfirm")
