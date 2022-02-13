import os
import sys

import src.utils.dirs as dirs


def install_main():
    os.system("sudo apt install git curl wget -y")


def install_snap():
    os.system("sudo apt update")
    os.system("sudo apt install snapd")
