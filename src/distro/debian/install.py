import os
import sys

# import src.utils.db as db
# import src.utils.dirs as dirs
from . import utils


class others:
    def better_discord():
        os.system(
            "curl -O https://raw.githubusercontent.com/bb010g/betterdiscordctl/master/betterdiscordctl")
        os.system("chmod +x betterdiscordctl")
        os.system("sudo mv betterdiscordctl /usr/local/bin")

    def teams():
        os.system(
            "curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -")
        os.system(
            """sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/ms-teams stable main" > /etc/apt/sources.list.d/teams.list'""")
        os.system("sudo apt update")
        os.system("sudo apt install teams")

    def zoom():
        os.system("wget https://zoom.us/client/latest/zoom_amd64.deb")
        os.system("sudo apt install ./zoom_amd64.deb")
        os.system("rm -f ./zoom_amd64.deb")

    def sublime_text():
        os.system(
            """wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -""")
        os.system("""sudo apt-get install apt-transport-https""")
        os.system(
            """echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list""")
        os.system("sudo apt update -y")
        os.system("sudo apt install sublime-text -y")

    def vscode():
        os.system(
            "wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg")
        os.system(
            "sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/")
        os.system(
            """sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'""")
        os.system("rm -f packages.microsoft.gpg")
        os.system("sudo apt install apt-transport-https")
        os.system("sudo apt update")
        os.system("sudo apt install code")

    def spotify():
        os.system(
            "curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add - ")
        os.system(
            """echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list""")
        os.system("sudo apt-get update && sudo apt-get install spotify-client")

    def shotcut():
        os.system("sudo add-apt-repository ppa:haraldhv/shotcut")
        os.system("sudo apt-get update && sudo apt-get upgrade")
        os.system("sudo apt install shotcut")

    def google_chrome():
        os.system(
            "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
        os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb")

    def minecraft():
        os.system("wget https://launcher.mojang.com/download/Minecraft.deb")
        os.system("sudo dpkg -i Minecraft.deb")
        os.system("sudo apt -f install -y")
        os.system("rm -f ./Minecraft.deb")

    def github_desktop():
        os.system("sudo wget https://github.com/shiftkey/desktop/releases/download/release-2.9.3-linux3/GitHubDesktop-linux-2.9.3-linux3.deb")
        os.system("sudo gdebi GitHubDesktop-linux-2.9.3-linux3.deb")

    def virtualbox():
        os.system(
            "wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -")
        os.system(
            'sudo add-apt-repository "deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib"')
        os.system("sudo apt update && sudo apt install virtualbox")

    def anydesk():
        os.system(
            "wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | sudo apt-key add -")
        os.system(
            'echo "deb http://deb.anydesk.com/ all main" | sudo tee /etc/apt/sources.list.d/anydesk-stable.list')
        os.system("sudo apt update")
        os.system("sudo apt install anydesk")

    def teamviewer():
        os.system(
            'wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb')
        os.system('sudo dpkg -i ./teamviewer_amd64.deb')
        os.system('rm -f ./teamviewer_amd64.deb')

    def tor_browser():
        os.system("sudo add-apt-repository ppa:micahflee/ppa")
        os.system("sudo apt update")
        os.system("sudo apt install torbrowser-launcher")


def installPackage(args: list = None, noconfirm: bool = False):
    if args is None:
        sys.exit("[E] Please enter the package names to install")

    final_command = utils.process_final_command(args=args, checks=(
        "-S",
        "-Sy"
    ))

    if "betterdiscord" in final_command:
        others.better_discord()

    if "teams" in final_command:
        others.teams()

    if "zoom" in final_command:
        others.zoom()

    if "sublimetext" in final_command:
        others.sublime_text()

    if "vscode" in final_command:
        others.vscode()

    if "spotify" in final_command:
        others.spotify()

    if "shotcut" in final_command:
        others.shotcut()

    if "googlechrome" in final_command:
        others.google_chrome()

    if "minecraft" in final_command:
        others.minecraft()

    if "githubdesktop" in final_command:
        others.github_desktop()

    if "virtualbox" in final_command:
        others.virtualbox()

    if "anydesk" in final_command:
        others.anydesk()

    if "teamviewer" in final_command:
        others.teamviewer()

    if "torbrowser" in final_command:
        others.tor_browser()

    if noconfirm:
        os.system(f"apt install {final_command} -y")
    else:
        os.system(f"apt install {final_command}")
