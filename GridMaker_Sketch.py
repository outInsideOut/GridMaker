import json
import GridMakerLib

# takes a json <dict>entries and constructs an object from it
# !! FEED ME GOOD JSON ONLY !!

###############################
# Qualifying.json:
# JSON_DATA::sessionResult.leaderBoardLines.racenumber

# EntryList.json:
# JSON_DATA::entries
###############################


qualiFile = "Qualifying.json"
entryListFile = "EntryList.json"
carOrder = []

quali = GridMakerLib.readJsonFile(qualiFile)
entryList = GridMakerLib.readJsonFile(entryListFile)

carOrder = GridMakerLib.parseQualiResults(quali)

entries = GridMakerLib.makeGridEntryList(carOrder, entryList)


with open("updatedEntryList.json", "w") as json_file:
    json.dump({"entries": entries}, json_file)
