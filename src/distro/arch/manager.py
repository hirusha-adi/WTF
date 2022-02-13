import os
import sys

from . import dependencies, install, remove, showlist, updates, custom


def runArchInstaller():
    sys_argv = sys.argv
    all_args = sys_argv[1:]
    sub_command = all_args[0].strip()

    # Install program
    # `yay -S package1 package2`
    if sub_command == "install":
        install.installPackage(args=all_args[1:])

    # Force Install (install without confirmation)
    # `yay -S package1 package2 --noconfirm`
    elif (sub_command in ("installf", "finstall", "force-install",
                          "forceinstall", "installforce",
                          "install-force")):
        install.installPackageForce(args=all_args[1:])

    # Remove program
    # `yay -R package1 package2`
    elif (sub_command in ("remove", "uninstall")):
        remove.removePackage(args=all_args[1:])

    # Remove Program with dependencies
    # `yay -Rs package1 package2`
    elif (sub_command in ("allremove", "removeall", "all-remove",
                          "remove-all", "removea")):
        remove.removePackageWithDependencies(args=all_args[1:])

    # List all installed packages
    # `yay -Q`
    elif (sub_command in ("list", "showall", "show-all",
                                  "list-all", "listall")):
        showlist.listPackages()

    # Update Repos (skip if already upto date)
    # `yay -Sy`
    elif (sub_command in ("update", "upd")):
        updates.updateSystem()

    # Update Repos (download again even if upto date)
    # `yay -Syy`
    elif (sub_command in ("updatef", "fupdate", "forceupdate",
                          "updateforce", "update-force",
                          "force-update")):
        updates.updateSystemForce()

    # Upgrade package
    # `yay -Su`
    elif (sub_command in ("upgrade", "upgrade-system", "upgr")):
        updates.upgradeSystem()

    # Full Upgrade
    # can fix some issues if any...
    # `yay -Syyuu`
    elif (sub_command in ("fupgrade", "upgradef", "forceupgrade",
                          "upgradeforce", "force-upgrade",
                          "upgrade-force", "full-upgrade",
                          "upgrade-full", "upgrade-fix", "fix-upgrade",
                          "upgradefull", "fullupgrade",
                          "fixupgrade", "upgradefix")):
        updates.fullUpgrade()

    # Install the needed dependencies
    # `sudo pacman -Sy base-devel git`
    # and install `yay`
    elif (sub_command in ("setup", "setup-wtf", "setupwtf",
                          "wtf", "wtfsetup", "dependencies")):
        dependencies.install_main()
        dependencies.install_yay()

    else:
        custom.runCustom(all_args)
