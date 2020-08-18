
import shutil
import os

# set where the source of the files are
source = "C:/Users/gonza/OneDrive/Desktop/Folder A/"

# set the destination path to folder B
destination = "C:/Users/gonza/OneDrive/Desktop/Folder B/"
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
