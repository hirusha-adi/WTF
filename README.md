# WTF

Linux Package Manager Wrapper to use the sampe commands on many distro's

# Usage

- ## Arch Linux

```
Commands:
    install         Install a Package
    installf        Install a Package without Confirmation
    remove          Remove a Package
    removeall       Remo a Package with Saved Data
    list            Display all installed packages
    update          Update Repo's
    updatef         Update Repo's (Force)
    upgrade         Upgrade all packages
    upgradef        Update and Upgrade System
    setup           Setup WTF
```

- ## Debain/Ubuntu

```
Commands:
    install         Install a Package
    installf        Install a Package without Confirmation
    remove          Remove a Package
    removeall       Remo a Package with Saved Data
    list            Display all installed packages
    update          Update Repo's
    upgrade         Upgrade System Packages
    upgradeforce    Upgrade System Packages without Confirmation
    snap            Run a custom snap command
    setup           Setup WTF
```

# Wrapped Around:

- ## Arch Linux

  1. `yay`

- ## Debian/Ubuntu
  1. `apt` (mainly)
  2. `snap`
