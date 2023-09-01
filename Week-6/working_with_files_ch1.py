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
