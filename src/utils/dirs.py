import os
from getpass import getuser


def chdirMain():
    username = str(getuser())
    if username.strip() == "root":
        root_homedir = os.path.join("/", "root")
        if not("wtftemp" in os.listdir(root_homedir)):
            os.mkdir("wtftemp")
        workdir = os.path.join(root_homedir, "wtftemp")
    else:
        homedir = os.path.join("/", "home", username)
        if not("wtftemp" in os.listdir(homedir)):
            os.mkdir("wtftemp")
        workdir = os.path.join(homedir, "wtftemp")
    return workdir
