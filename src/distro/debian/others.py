import os


def fixBroken():
    os.system("sudo apt --fix-missing update")
    os.system("sudo apt update")
    os.system("sudo apt install -f")
