import os


def updateSystem():
    os.system("yay -Sy")


def updateSystemForce():
    os.system("yay -Syy")


def upgradeSystem():
    os.system("yay -Su")


def fullUpgrade():
    os.system("yay -Syyuu")
