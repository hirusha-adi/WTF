import os
import sys

import src.utils.db as db
import src.utils.dirs as dirs


def install_main():
    os.system("sudo pacman -Sy git base-devel")


def install_yay():
    dirs.chdirMain()
    os.system("git clone https://aur.archlinux.org/yay.git")
    os.chdir(os.path.join(os.getcwd(), "yay"))
    os.system("makepkg -si")
    os.chdir("..")
    os.system("rm -rf ./yay")
