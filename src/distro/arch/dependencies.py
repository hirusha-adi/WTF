import os
import sys

import src.utils.dirs as dirs


def install_main():
    os.system("sudo pacman -Sy curl wget git base-devel --noconfirm")


def install_yay():
    dirs.chdirMain()
    os.system("git clone https://aur.archlinux.org/yay.git")
    os.chdir(os.path.join(os.getcwd(), "yay"))
    os.system("makepkg -si")
    os.chdir("..")
    os.system("rm -rf ./yay")
