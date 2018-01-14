from collections import OrderedDict

GENDER = [
    "Male",
    "Female",
    "Unknown"
]
GENDER2 = [
    "Male",
    "Female",
    "Unknown"
]
GENDER3 = [
    "Male",
    "Female",
    "Unknown"
]
GENDER4 = [
    "Male",
    "Female",
    "Unknown"
]
GENDER5 = [
    "Male",
    "Female",
    "Unknown"
]


GROUP_1 = OrderedDict()
GROUP_1["Gender"] = GENDER
GROUP_1["Gender2"] = GENDER2
GROUP_1["Gender3"] = GENDER3
GROUP_1["Gender4"] = GENDER4
GROUP_1["Gender5"] = GENDER5


print(GROUP_1.values()[0])
