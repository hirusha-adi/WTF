import os
from getpass import getuser

import src.utils.db as db


DEBUG = db.main.debug


def chdirMain():
    username = str(getuser())
    if username.strip() == "root":
        if DEBUG:
            print(f"[D] Running as root")
        root_homedir = os.path.join("/", "root")
        if not("wtftemp" in os.listdir(root_homedir)):
            os.mkdir("wtftemp")
            if DEBUG:
                print(f"[D] Made `wtftemp` directory in  {homedir}")
        workdir = os.path.join(root_homedir, "wtftemp")
        if DEBUG:
            print(f"[D] Path: {workdir}")
            print(f"[D] Is Dir?: {os.path.isdir(workdir)}")
    else:
        if DEBUG:
            print(f"[D] Not running as root")
        homedir = os.path.join("/", "home", username)
        if DEBUG:
            print(f"[D] Setting default home dir to {homedir}")
        if not("wtftemp" in os.listdir(homedir)):
            os.mkdir("wtftemp")
            if DEBUG:
                print(f"[D] Made `wtftemp` directory in  {homedir}")
        workdir = os.path.join(homedir, "wtftemp")
        if DEBUG:
            print(f"[D] Path: {workdir}")
            print(f"[D] Is Dir?: {os.path.isdir(workdir)}")
    return workdir
