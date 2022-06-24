import json
import os
import hashlib
import tkinter as tk
from tkinter import filedialog
from shutil import copytree



script_dir = os.path.dirname(__file__)
relpath = "copy_put_playerdata_here/PlayerData.dat"

playerdatafilepath = os.path.join(script_dir, relpath)

if not os.path.exists(playerdatafilepath):
    print("PlayerData.dat was not found in the folder copy_put_playerdata_here")
    exit()

playerdatafile = open(playerdatafilepath)


playerdata = json.load(playerdatafile)

print("Please open your custom songs folder path (so the path of the Folder CustomLevels")

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory(title="Select Custom Songs folder")

if file_path == "":
    exit()

print("Custom song path: " + file_path)

favorites_list = []

for i in playerdata['localPlayers']:
    for j in i['favoritesLevelIds']:
        favorites_list.append(j)

output_path = filedialog.askdirectory(title="Select Output directory")

if output_path == "":
    exit()

listdir = os.listdir(file_path)


for path in listdir:
    fromfolderpath = os.path.join(file_path, path)

    # if not path.startswith("268a1"):
    #     continue

    if not os.path.isdir(fromfolderpath):
        continue

    datainfopath = os.path.join(file_path ,path, "Info.dat")
    datainfofile = open(datainfopath)
    datafile = json.load(datainfofile)

    beatMapsFileNames = []

    for i in datafile["_difficultyBeatmapSets"]:
        for j in i["_difficultyBeatmaps"]:
            filenamestring = j["_beatmapFilename"]
            beatMapsFileNames.append(filenamestring)

    datainfofile = open(datainfopath)
    datainfostring = datainfofile.read()

    completeHashString = datainfostring

    for beatpath in beatMapsFileNames:
        diffpath = os.path.join(file_path, path, beatpath)
        difffile = open(diffpath)

        diffstring = difffile.read()
        completeHashString = completeHashString + diffstring

    sha_1 = hashlib.sha1()
    sha_1.update(completeHashString.encode('utf-8'))
    outputhash = sha_1.hexdigest()

    outputstring = "custom_level_" + outputhash.upper()

    if outputstring in favorites_list:
        tofolderpath = os.path.join(output_path, path)

        copytree(fromfolderpath, tofolderpath)