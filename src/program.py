import src.distro.arch.manager as arch_manager
import src.distro.debian.manager as debian_manager
from utils import distro


def startProgram():
    distro_cur = distro.checkDistro_Simple()
    if distro_cur == "ubuntu":
        debian_manager.runDebianInstaller()
    elif distro_cur == "debian":
        debian_manager.runDebianInstaller()
    elif distro_cur == "arch":
        arch_manager.runArchInstaller()
