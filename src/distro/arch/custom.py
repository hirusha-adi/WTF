import os
import sys


def installPackage(args: list = None):
    if args is None:
        sys.exit("[E] Please enter the args")

    final_command = ""
    for arg in args:
        final_command += f"{arg} "

    os.system(f"yay {final_command}")
