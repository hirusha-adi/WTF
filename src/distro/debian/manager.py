import os
import sys

from . import dependencies, install, remove, showlist, updates, custom


def runDebianInstaller():
    sys_argv = sys.argv
    all_args = sys_argv[1:]
    sub_command = all_args[0].strip()

    # Install program
    # `sudo apt install package1 package2`
    if sub_command == "install":
        install.installPackage(args=all_args[1:],
                               noconfirm=False)

    # Force Install (install without confirmation)
    # `sudo apt install package1 package2 -y`
    elif (sub_command in ("installf", "finstall", "force-install",
                          "forceinstall", "installforce",
                          "install-force")):
        install.installPackage(args=all_args[1:],
                               noconfirm=True)

    # Remove program
    # `sudo apt remove package1 package2`
    elif (sub_command in ("remove", "uninstall")):
        remove.removePackage(args=all_args[1:])

    # Remove Program with dependencies
    # `sudo apt purge package1 package2`
    elif (sub_command in ("allremove", "removeall", "all-remove",
                          "remove-all", "removea")):
        remove.removePackageWithSaveData(args=all_args[1:])

    # List all installed packages
    # `sudo dpkg --list`
    elif (sub_command in ("list", "showall", "show-all",
                                  "list-all", "listall")):
        showlist.listPackages()

    # Update Repos (skip if already upto date)
    # `sudo apt update`
    elif (sub_command in ("update", "upd")):
        updates.updateSystem()

    # Upgrade package
    # `sudo apt upgrade`
    # `sudo snap refresh`
    elif (sub_command in ("upgrade", "upgrade-system", "upgr")):
        updates.upgradeSystem()

    # Full Upgrade
    # can fix some issues if any...
    # `sudo apt update && sudo apt upgrade -y`
    # `sudo snap refresh`
    elif (sub_command in ("fupgrade", "upgradef", "forceupgrade",
                          "upgradeforce", "force-upgrade",
                          "upgrade-force", "full-upgrade",
                          "upgrade-full", "upgrade-fix",
                          "upgradefull", "fullupgrade")):
        updates.fullUpgrade()

    # Install the needed dependencies
    # `sudo apt install git curl wget -y`
    # `sudo apt install snapd`
    elif (sub_command in ("setup", "setup-wtf", "setupwtf",
                          "wtf", "wtfsetup", "dependencies")):
        dependencies.install_main()
        dependencies.install_snap()

    elif (sub_command == "snap"):
        custom.runSnap(args=all_args)

    else:
        custom.runCustom(args=all_args)
