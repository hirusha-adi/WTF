import os


def updateSystem():
    os.system("yay -Sy")


def upgradeSystem():
    os.system("yay -Su")


def fullUpgrade():
    os.system("yay -Syyuu")
