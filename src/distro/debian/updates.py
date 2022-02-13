import os


def updateSystem():
    os.system("sudo apt update")


def updateSystemForce():
    os.system("sudo apt update -y")


def upgradeSystem():
    os.system("sudo apt upgrade")


def fullUpgrade():
    os.system("sudo apt update && sudo apt upgrade")
