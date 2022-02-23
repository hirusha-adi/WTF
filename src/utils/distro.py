import sys
import subprocess


def uname_a():
    try:
        unamea = subprocess.check_output(["uname -a"], shell=True)
    except subprocess.CalledProcessError as subperr:
        unamea = False
        print("Error Code", subperr.returncode, subperr.output)
    return unamea


def checkDistro_Simple():
    uname = uname_a().decode()
    if "Ubuntu" in uname:
        return "ubuntu"
    elif "Debian" in uname:
        return "debian"
    elif "Arch" in uname:
        return "arch"
    else:
        sys.exit("[!!] This Distro is not supported yet...")
