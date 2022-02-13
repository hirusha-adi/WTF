import os
import sys

# import src.utils.db as db
# import src.utils.dirs as dirs
from . import custom, utils


def installPackage(args: list = None):
    if args is None:
        sys.exit("[E] Please enter the package names to install")

    final_command = utils.process_final_command(args=args, checks=(
        "-S",
        "-Sy"
    ))

    if "betterdiscord" in final_command:
        custom.install_betterDiscord()
        print("[+] run `betterdiscordctl` to start better-discord")

    os.system(f"yay -S {final_command}")


def installPackageForce(args: list = None):
    if args is None:
        sys.exit("[E] Please enter the package names to install")

    final_command = utils.process_final_command(args=args, checks=(
        "-S",
        "--noconfirm"
    ))

    if "betterdiscord" in final_command:
        custom.install_betterDiscord()
        print("[+] run `betterdiscordctl` to start better-discord")

    os.system(f"yay -S {final_command} --noconfirm")
