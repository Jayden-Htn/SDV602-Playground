# Following the Linkedin course: Working with Files (2021) by Kathryn Hodge.
# I have used Python's file system before, but this will be much more in-depth then my current knowkedge.


# <---- 1: Accessing Directory and File Details ---->


# 1.1: Understanding the file system

# absolute path: the full path to a file or directory containing the root node and no context
# relative path: the path to a file or directory relative to the current working directory


# 1.2: Navigate the file system using an os module

# import os

def display_cwd():
    # cwd = current working directory
    cwd = os.getcwd()
    print('\nCurrent working directory:', cwd)

def up_one_directory_level():
    os.chdir('../') # changes the cwd to the parent directory
    # chdir = change directory

def display_entries_in_directory(directory):
    # scandir = scan directory
    # scandir is an iterator, so it can be used in a for loop
    print('\nEntries in directory:', directory)
    with os.scandir(directory) as entries:
        for entry in entries:
            print(entry.name)
    # could use listdir() but it shows less information
    # scandir is more efficient than listdir as it doesn't load all the information into memory 

if __name__ == "__main__":
    pass
    # display_cwd()
    # up_one_directory_level()
    # display_cwd()
    # display_entries_in_directory('SDV601-Playground/Week-6/')


# 1.3: Use os module to uncover path and file details

# can get details like: file size, date modified, date created, permissions, etc.

from datetime import datetime
import os

def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formated_date = utc_timestamp.strftime('%d %b %Y %H:%M:%S')
    return formated_date

def display_entries_in_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            print("Name:", entry.name) # name = name of the file
            info = entry.stat() # stat = statistics objects of the file
            print("Creation time:", format_datetime(info.st_ctime)) # st_ctime = creation time command for Windows OS
            print("Last access time:", format_datetime(info.st_atime)) # st_atime = last access time command for Windows OS
            print("Size:", info.st_size, "bytes") # st_size = size of the file in bytes

def display_directories(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            # is_dir() = returns True if the entry is a directory (folder)
            if entry.is_dir():
                print("Directory name:", entry.name)

def display_files(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            # is_file() = returns True if the entry is a file
            if entry.is_file():
                print("File name:", entry.name)

if __name__ == "__main__":
    pass
    # display_entries_in_directory('Week-6/')
    # display_directories('./')
    # display_files('./')


# 1.4: Filter path names with glob module

# import glob # glob = global, searches the current directory for files

def display_png():
    png_files = glob.glob('*.png') # glob = global, searches the current directory for files
    # '../**/*.png' = recursive=True, will search all subdirectories
    
def find_monster_one():
    filtered_item = glob.glob('*monster01*') # finds all files with monster01 in the name

def find_in_subdirectory():
    for item in glob.iglob('**/*monster01*', recursive=True): # iglob = iterator glob, returns an iterator instead of a list
        print(item)

if __name__ == "__main__":
    pass
    # display_png() # because of file structure, won't work
    # find_monster_one() # because of file structure, won't work
    # find_in_subdirectory() # large output


# 1.5: Recursively list all files in a directory

# import os

# os.walk = generate files names in a directory tree by walking the tree either top-down or bottom-up

def top_down_walk():
    for dirpath, dirnames, files in os.walk('Week-6'): # returns a generator object
        print('Current path:', dirpath)
        print('Sub directories:')
        for dirname in dirnames:
            print(dirname)
        print('Files:')
        for file in files:
            print(file)
        print()

def bottom_up_walk():
    for dirpath, dirnames, files in os.walk('Week-6', topdown=False): # returns a generator object
        print('Current path:', dirpath)
        print('Sub directories:')
        for dirname in dirnames:
            print(dirname)
        print('Files:')
        for file in files:
            print(file)
        print()

if __name__ == "__main__":
    pass
    # top_down_walk()
    # bottom_up_walk()


# 1.6 Understand Python's new pathlib module

# from pathlib import Path

def print_directory_path():
    entries = Path.cwd() # cwd = current working directory

    # specify specifc directory with path, relatve or absolute
    # entries = Path('Week-6/')
    # entries = Path.home() # home = home directory of the user

    for entry in entries.iterdir(): # iterdir = creates an iterator of the entries in the directory
        print(entry.name) # e.g. monster.png
        print(entry.parent) # parent = parent directory of the entry, e.g. /Users/practice/Week-6
        print(entry.parent.parent) # parent.parent = parent directory of the parent directory of the entry, e.g. /Users/practice
        print(entry.stem) # stem = name of the entry without the extension, e.g. monster
        print(entry.suffix) # suffix = extension of the entry, e.g. .png
        print(entry.stat()) # stat = statistics objects of the file

if __name__ == "__main__":
    pass
    # print_directory_path()

    
# 1.7: Create directories in Python

import os
from pathlib import Path

def make_logs_dir():
    try:
        os.mkdir('logs/') # mkdir = make directory
        # can use absolute or relative path
    except FileExistsError as ex:
        print('Logs directory already exists')
    
def make_output_dir():
    dir_path = Path('output/')
    dir_path.mkdir(exist_ok=True) # mkdir = make directory

if __name__ == "__main__":
    pass
    # make_logs_dir() # error?
    make_output_dir() # error?


