import os
import sys

from . import utils


def runCustom(args: list = None):
    if args is None:
        sys.exit("[E] Please enter the args")

    final_command = utils.process_final_command(args=args, checks=(
        "wtf",
        "./wtf"
    ))

    os.system(f"sudo apt {final_command}")


def runSnap(args: list = None):
    if args is None:
        sys.exit("[E] Please enter the args")

    final_command = utils.process_final_command(args=args, checks=(
        "wtf",
        "./wtf"
    ))

    os.system(f"sudo snap {final_command}")
