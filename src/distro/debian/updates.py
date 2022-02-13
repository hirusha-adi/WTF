import os


def updateSystem():
    os.system("sudo apt update")


def updateSystemForce():
    os.system("sudo apt update")


def upgradeSystem():
    os.system("sudo apt upgrade")
    os.system("sudo snap refresh")


def fullUpgrade():
    os.system("sudo apt update && sudo apt upgrade -y")
    os.system("sudo snap refresh")
