import os
import sys
import requests


def runCustom(args: list = None):
    if args is None:
        sys.exit("[E] Please enter the args")

    final_command = ""
    for arg in args:
        final_command += f"{arg} "

    os.system(f"yay {final_command}")


def install_betterDiscord():
    data = requests.get(
        "https://raw.githubusercontent.com/bb010g/betterdiscordctl/master/betterdiscordctl").content
    with open("betterdiscordctl", "wb") as file:
        file.write(data)
    os.system("chmod +x betterdiscordctl")
    os.system("sudo mv betterdiscordctl /usr/local/bin")
