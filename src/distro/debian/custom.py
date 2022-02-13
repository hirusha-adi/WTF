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


def install_betterDiscord():
    os.system(
        "curl -O https://raw.githubusercontent.com/bb010g/betterdiscordctl/master/betterdiscordctl")
    os.system("chmod +x betterdiscordctl")
    os.system("sudo mv betterdiscordctl /usr/local/bin")
