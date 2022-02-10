import csv
import sys


def getAllInfo():
    RELEASE_DATA = {}
    with open("/etc/os-release", "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="=")
        for row in reader:
            if row:
                RELEASE_DATA[row[0]] = row[1]
    if RELEASE_DATA["ID"] in ["debian", "raspbian"]:
        with open("/etc/debian_version") as f:
            DEBIAN_VERSION = f.readline().strip()
        major_version = DEBIAN_VERSION.split(".")[0]
        version_split = RELEASE_DATA["VERSION"].split(" ", maxsplit=1)
        if version_split[0] == major_version:
            RELEASE_DATA["VERSION"] = " ".join(
                [DEBIAN_VERSION] + version_split[1:])
    return RELEASE_DATA


class Distro:
    allInfo = getAllInfo()
    try:
        NAME = allInfo["NAME"]
    except KeyError:
        NAME = None

    try:
        PRETTY_NAME = allInfo["PRETTY_NAME"]
    except KeyError:
        PRETTY_NAME = allInfo["PRETTY_NAME"]

    try:
        ID = allInfo["ID"]
    except KeyError:
        ID = allInfo["ID"]

    try:
        BUILD_ID = allInfo["BUILD_ID"]
    except KeyError:
        BUILD_ID = allInfo["BUILD_ID"]

    try:
        ANSI_COLOR = allInfo["ANSI_COLOR"]
    except KeyError:
        ANSI_COLOR = allInfo["ANSI_COLOR"]

    try:
        HOME_URL = allInfo["HOME_URL"]
    except KeyError:
        HOME_URL = allInfo["HOME_URL"]

    try:
        DOCUMENTATION_URL = allInfo["DOCUMENTATION_URL"]
    except KeyError:
        DOCUMENTATION_URL = allInfo["DOCUMENTATION_URL"]

    try:
        SUPPORT_URL = allInfo["SUPPORT_URL"]
    except KeyError:
        SUPPORT_URL = allInfo["SUPPORT_URL"]

    try:
        BUG_REPORT_URL = allInfo["BUG_REPORT_URL"]
    except KeyError:
        BUG_REPORT_URL = allInfo["BUG_REPORT_URL"]

    try:
        LOGO = allInfo["LOGO"]
    except KeyError:
        LOGO = allInfo["LOGO"]

    try:
        IMAGE_ID = allInfo["IMAGE_ID"]
    except KeyError:
        IMAGE_ID = allInfo["IMAGE_ID"]

    try:
        IMAGE_VERSION = allInfo["IMAGE_VERSION"]
    except KeyError:
        IMAGE_VERSION = allInfo["IMAGE_VERSION"]


def getName():
    try:
        return getAllInfo()["NAME"]
    except KeyError:
        return sys.exit("")


def getPrettyName():
    try:
        return getAllInfo()["PRETTY_NAME"]
    except KeyError:
        return None


def getID():
    try:
        return getAllInfo()["ID"]
    except KeyError:
        return None


def getBuildID():
    try:
        return getAllInfo()["BUILD_ID"]
    except KeyError:
        return None


def getAnsiColor():
    try:
        return getAllInfo()["ANSI_COLOR"]
    except KeyError:
        return None


def getHomeUrl():
    try:
        return getAllInfo()["HOME_URL"]
    except KeyError:
        return None


def getDocumentationUrl():
    try:
        return getAllInfo()["DOCUMENTATION_URL"]
    except KeyError:
        return None


def getSupportUrl():
    try:
        return getAllInfo()["SUPPORT_URL"]
    except KeyError:
        return None


def getBugReportUrl():
    try:
        return getAllInfo()["BUG_REPORT_URL"]
    except KeyError:
        return None


def getLogo():
    try:
        return getAllInfo()["LOGO"]
    except KeyError:
        return None


def getImageID():
    try:
        return getAllInfo()["IMAGE_ID"]
    except KeyError:
        return None


def getImageVersion():
    try:
        return getAllInfo()["IMAGE_VERSION"]
    except KeyError:
        return None
