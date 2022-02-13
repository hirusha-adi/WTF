import os


def listPackages(lookingfor=None):
    if lookingfor is None:
        os.system("dpkg --list")
    else:
        if isinstance(lookingfor, str):
            os.system(f"dpkg --list | grep {lookingfor}")
        else:
            os.system(f"dpkg --list | grep {' '.join(lookingfor)}")
