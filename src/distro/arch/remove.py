import os
import sys

# import src.utils.db as db
# import src.utils.dirs as dirs


def removePackage():
    try:
        program_names_all = sys.argv[2:]
    except IndexError:
        sys.exit("[E] Please enter the package names to remove")
    for program_name in program_names_all:
        os.system(f"yay -R {program_name}")


def removePackageWithDependencies():
    try:
        program_names_all = sys.argv[2:]
    except IndexError:
        sys.exit("[E] Please enter the package names to remove")
    for program_name in program_names_all:
        os.system(f"yay -Rs {program_name}")
