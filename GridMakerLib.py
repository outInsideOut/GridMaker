import json
from pprint import pprint


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def readJsonFile(file):
    with open(file, 'r') as openFile:
        return json.load(openFile)


def parseQualiResults(quali):
    carOrder = []
    print("Grid order (car numbers):")
    for entry in quali["sessionResult"]["leaderBoardLines"]:
        entryData = Struct(**entry)
        carOrder.append(Struct(**(entryData.car)).raceNumber)
        print(Struct(**(entryData.car)).raceNumber)
    return carOrder


def makeGridEntryList(carOrder, entryList):
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
    return entries
