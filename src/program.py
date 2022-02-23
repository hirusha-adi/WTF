import src.distro.arch.manager as arch_manager
import src.distro.debian.manager as debian_manager
from src.utils import distro
from src.utils import helps


def startProgram():
    distro_cur = distro.checkDistro_Simple()
    if (distro_cur == "ubuntu") or (distro_cur == "debian"):
        try:
            debian_manager.runDebianInstaller()
        except IndexError:
            print(helps.__DEBIAN__)
    elif distro_cur == "arch":
        try:
            arch_manager.runArchInstaller()
        except IndexError:
            print(helps.__ARCH__)
