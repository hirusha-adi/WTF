import os
import sys

# import src.utils.db as db
# import src.utils.dirs as dirs


def installPackage(args: list = None):
    # Old Standalone Code
    # Not very synced with commands in yay
    # ------------------------------
    # try:
    #     program_names_all = sys.argv[2:]
    # except IndexError:
    #     sys.exit("[E] Please enter the package names to install")
    # for program_name in program_names_all:
    #     os.system(f"yay -S {program_name}")

    # New Code
    if args is None:
        sys.exit("[E] Please enter the package names to install")

    final_command = ""
    for arg in args:
        # to prevent passing the same argument twice
        if str(arg).strip().startswith("-S"):
            continue
        final_command += f"{arg} "

    os.system(f"yay -S {final_command}")


def installPackageForce():
    try:
        program_names_all = sys.argv[2:]
    except IndexError:
        sys.exit("[E] Please enter the package names to install")
    for program_name in program_names_all:
        os.system(f"yay -S {program_name}")
