import json

with open("settings.json", "r", encoding="utf-8") as _dfile:
    data = json.load(_dfile)


class main:
    debug = data["DEBUG"]
