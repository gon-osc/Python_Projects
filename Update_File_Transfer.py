import time
import shutil
import os


SECONDS_IN_DAY = 24 * 60 * 60

# set where the source of the files are
source = "C:/Users/gonza/OneDrive/Desktop/Folder A/"

# set the destination path to folder B
destination = "C:/Users/gonza/OneDrive/Desktop/Folder B/"


now = time.time()
before = now - SECONDS_IN_DAY

def last_mod_time(fname):
    return os.path.getmtime(fname)

for fname in os.listdir(source):
    source_fname = os.path.join(source, fname)
    if last_mod_time(source_fname) > before:
        destination_fname = os.path.join(destination, fname)
        shutil.move(source_fname, destination_fname)
