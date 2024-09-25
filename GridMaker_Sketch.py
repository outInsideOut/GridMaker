import json
from pprint import pprint

# takes a json <dict>entries and constructs an object from it
# !! FEED ME GOOD JSON ONLY !!


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def readJsonFile(file):
    with open(file, 'r') as openFile:
        return json.load(openFile)


qualiFile = "Qualifying.json"
entryListFile = "EntryList.json"
carOrder = []

quali = readJsonFile(qualiFile)
entryList = readJsonFile(entryListFile)

print("Grid order (car numbers):")
for entry in quali["sessionResult"]["leaderBoardLines"]:
    entryData = Struct(**entry)
    carOrder.append(Struct(**(entryData.car)).raceNumber)
    print(Struct(**(entryData.car)).raceNumber)

entries = []

print("EntryList cars with Grid Spots:")
for entry in entryList["entries"]:
    entryData = Struct(**entry)
    try:
        raceNumber = entryData.raceNumber
    except:
        pprint(vars(entryData))
        entries.append(entryData.__dict__)
        continue

    if carOrder.__contains__(raceNumber):
        gridSpot = carOrder.index(raceNumber) + 1
    else:
        gridSpot = -1

    print("#: " + str(entryData.raceNumber) +
          "\t--- Pos: " + str(gridSpot))

    entryData.defaultGridPosition = gridSpot
    entries.append(entryData.__dict__)


with open("updatedEntryList.json", "w") as json_file:
    json.dump({"entries": entries}, json_file)
