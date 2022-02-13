import os
import sys

from . import dependencies, install, remove, showlist, updates, custom


def runArchInstaller():
    all_args = sys.argv[1:]

    # Install program
    # `yay -S package1 package2`
    if all_args[0].strip() == "install":
        install.installPackage(args=all_args[1:])

    # Force Install (install without confirmation)
    # `yay -S package1 package2 --noconfirm`
    elif (all_args[0].strip() in ("installf", "finstall", "force-install",
                                  "forceinstall", "installforce",
                                  "install-force")):
        install.installPackageForce(args=all_args[1:])

    # Remove program
    # `yay -R package1 package2`
    elif (all_args[0].strip() in ("remove", "uninstall")):
        remove.removePackage(args=all_args[1:])

    # Remove Program with dependencies
    # `yay -Rs package1 package2`
    elif (all_args[0].strip() in ("allremove", "removeall", "all-remove",
                                  "remove-all", "removea")):
        remove.removePackageWithDependencies(args=all_args[1:])

    # List all installed packages
    # `yay -Q`
    elif (all_args[0].strip() in ("list", "showall", "show-all",
                                  "list-all", "listall")):
        showlist.listPackages()

    # Update Repos (skip if already upto date)
    # `yay -Sy`
    elif (all_args[0].strip() in ("update", "upd")):
        updates.updateSystem()

    # Update Repos (download again even if upto date)
    # `yay -Syy`
    elif (all_args[0].strip() in ("updatef", "fupdate", "forceupdate",
                                  "updateforce", "update-force",
                                  "force-update")):
        updates.updateSystemForce()

    # Upgrade package
    # `yay -Su`
    elif (all_args[0].strip() in ("upgrade", "upgrade-system", "upgr")):
        updates.upgradeSystem()

    # Full Upgrade
    # can fix some issues if any...
    # `yay -Syyuu`
    elif (all_args[0].strip() in ("fupgrade", "upgradef", "forceupgrade",
                                  "upgradeforce", "force-upgrade",
                                  "upgrade-force", "full-upgrade",
                                  "upgrade-full", "upgrade-fix", "fix-upgrade",
                                  "upgradefull", "fullupgrade",
                                  "fixupgrade", "upgradefix")):
        updates.fullUpgrade()

    elif (all_args[0].strip() in ("setup", "setup-wtf", "setupwtf", "wtf", "wtfsetup")):
        dependencies.install_main()
        dependencies.install_yay()
