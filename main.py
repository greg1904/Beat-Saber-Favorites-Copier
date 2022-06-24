import json
import os
import tkinter as tk
from tkinter import filedialog


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

file_path = "" 

while file_path == "":
    file_path = filedialog.askdirectory()

print("Custom song path: " + file_path)

favorites_list = []

for i in playerdata['localPlayers']:
    for j in i['favoritesLevelIds']:
        favorites_list.append(j)

print(favorites_list)
print("custom_level_C46C1B32C3886EBE1E4F1245A2F7F304FEEBE21E" in favorites_list)