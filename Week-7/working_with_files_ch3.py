# Following the Linkedin course: Working with Files (2021) by Kathryn Hodge.
# I have used Python's file system before, but this will be much more in-depth then my current knowkedge.


# <---- 3: Writing to Files ---->

# 3.1: Write data to a file in Python

def write_content():
    with open('./Week-7/Exercise Files/03/num-series.txt', 'w') as w:
        for x in range(50):
            w.write(f'{x}\n')

def append_content():
    with open('./Week-7/Exercise Files/03/num-series.txt', 'a') as w:
        for x in range(50, 100):
            w.write(f'{x}\n')

if __name__ == "__main__":
    pass
    # write_content()
    # append_content()


# 3.2: Move and rename files with Python

# import os
# from pathlib import Path
# import shutil # shell utilities

def rename_os():
    os.rename('./Week-7/Exercise Files/03/num-series.txt', './Week-7/Exercise Files/03/num-series-100.txt')

def rename_pathlib():
    path = Path('./Week-7/Exercise Files/03/num-series-100.txt')
    path.rename('./Week-7/Exercise Files/03/num-series.txt')

def move_files():
    shutil.move('./Week-7/Exercise Files/03/', './Week-7/Exercise Files/three') 
    # moves folder to another folder

def move_files_back():
    shutil.move('./Week-7/Exercise Files/three/03/', './Week-7/Exercise Files/') 

def move_file():
    shutil.move('./Week-7/Exercise Files/03/num-series.txt', './Week-7/Exercise Files/three/') 
    # moves a single file

def move_file_back():
    shutil.move('./Week-7/Exercise Files/three/num-series.txt', './Week-7/Exercise Files/03/')

if __name__ == "__main__":
    pass
    # rename_os()
    # rename_pathlib() # leaves old file in directory
    # move_files()
    # move_files_back()
    # move_file()
    # move_file_back()


# 3.3: Copy with Python + 3.4: Delete files with Python

import shutil
import os
from pathlib import Path

def copy_file():
    shutil.copy('./Week-7/Exercise Files/03/num-series.txt', './Week-7/Exercise Files/three/')
    # copies file to new location

def copy_file_metadata():
    shutil.copy2('./Week-7/Exercise Files/03/num-series.txt', './Week-7/Exercise Files/three/')
    # copies metadata from original file

def copy_directory():
    shutil.copytree('./Week-7/Exercise Files/03/', './Week-7/Exercise Files/03-copy/')
    # copies directory and contents
    # can't copy to a directory that already exists

def delete_file_os():
    os.remove('./Week-7/Exercise Files/three/num-series.txt')
    # deletes file

def delete_file_pathlib():
    path = Path('./Week-7/Exercise Files/three/num-series.txt')
    path.unlink()
    # deletes file

def delete_directory_os():
    os.rmdir('./Week-7/Exercise Files/03-copy/')
    # deletes directory
    # rmdir = remove directory
    # directory must be empty

def delete_directory_pathlib():
    path = Path('./Week-7/Exercise Files/03-copy/')
    path.rmdir()
    # deletes directory
    # rmdir = remove directory
    # directory must be empty

def delete_directory_shutil():
    shutil.rmtree('./Week-7/Exercise Files/03-copy/')
    # deletes directory and contents

if __name__ == "__main__":
    pass
    # copy_file()
    # copy_file_metadata()
    # copy_directory()
    # delete_file_os()
    # delete_file_pathlib()
    # delete_directory_os()
    # delete_directory_pathlib()
    # delete_directory_shutil()
    # note: files deleted with Python are not sent to the trash, they are permanently deleted


# 3.4: Save tabular data with csv module

import csv

def write_to_csv_list():
    with open('./Week-7/Exercise Files/03/products.csv', 'w') as f:
        writer = csv.writer(f)
        # write individual rows
        writer.writerow(['ID', 'Name', 'Price'])
        writer.writerow([ 1, 'Monitor', 100])
        writer.writerow([ 2, 'Keyboard', 50])
        writer.writerow([ 3, 'Mouse', 25])

def write_to_csv_dict():
    with open('./Week-7/Exercise Files/03/maintenance-products.csv', 'w') as f:
        # set column headers
        headers = ['ID', 'Name', 'Price'] 
        # create a dictionary writer object
        writer = csv.DictWriter(f, fieldnames=headers)
        # write headers to file
        writer.writeheader()
        # write individual rows
        item = {'ID': 1, 'Name': 'Monitor', 'Price': 100}
        writer.writerow(item)

if __name__ == "__main__":
    pass
    # write_to_csv_list()
    # write_to_csv_dict()


# 3.5: Write data to a JSON file in Python

import json

def generate_dictionary(name, title, price, scariness):
    return {
        'name': name,
        'title': title,
        'price': price,
        'scariness': scariness
    }

def write_to_json(dict):
    with open('./Week-7/Exercise Files/03/monsters.json', 'w') as f:
        json.dump(dict, f, indent=2)
        # indent changes the number of spaces used for indentation
        # 2 is the standard

if __name__ == "__main__":
    pass
    monster_one = generate_dictionary('Chase', 'Stealthy sneaker', 50, 32)
    monster_two = generate_dictionary('Big J', 'Hooligan', 24, 12)
    monster_three = generate_dictionary('Whitefang', 'Intimidator', 100, 42)
    monster_four = generate_dictionary('Sneaky Pete', 'Sneaky sneaker', 50, 32)
    write_to_json([monster_one, monster_two, monster_three, monster_four])
