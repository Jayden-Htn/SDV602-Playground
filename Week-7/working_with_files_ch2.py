# Following the Linkedin course: Working with Files (2021) by Kathryn Hodge.
# I have used Python's file system before, but this will be much more in-depth then my current knowkedge.


# <---- 2: Processing Files ---->

# 2.1: Open files in Python

def print_content():
    f = open('Week-7/Exercise Files/02/02_01/description-01.txt', 'r') # open file in read mode
    contents = f.read() # read whole file
    print(contents)
    f.close() # close file

def write_content():
    # with is simpler and automatically closes the file
    with open('Week-7/Exercise Files/02/02_01/description-01.txt', 'w') as f: # open file in write mode
        f.write('This is a new line of text') # overwrites the file

if __name__ == "__main__":
    pass
    # print_content()
    # print("------------")
    # write_content()
    # print_content()


# 2.2: Read text files in Python

# f.read() # read whole file
# f.read(10) # read 10 characters/bytes
# f.readlines() # read all lines in file, returns a list
# f.readline() # read one line at a time, returns a string
# each time you call readline() it will read the next line (use loop)
# print(f.readline(), end='') # end='' removes the extra line break


# 2.3: Parse JSON files with Python

# JSON is a way to store data in a human-readable format
# JSON = JavaScript Object Notation
# uses key-value pairs

import json

def display_json():
    with open('./Week-7/Exercise Files/02/monster.json') as f:
        data = json.load(f)
        print(data)

def display_name():
    with open('./Week-7/Exercise Files/02/monster.json') as f:
        data = json.load(f)
        print("Welcome", data['monsterName'])

if __name__ == "__main__":
    pass
    # display_json()
    # display_name()


# 2.4: Read CSV files in Python with csv module and pandas

import csv
import pandas as pd

def display_csv():
    with open('./Week-7/Exercise Files/02/monsters.csv') as f:
        reader = csv.reader(f, delimiter=',') # delimiter is optional, default is comma
        for row in reader:
            print(row[1])

def display_csv_dict():
    with open('./Week-7/Exercise Files/02/monsters.csv') as f:
        reader = csv.DictReader(f, delimiter=',') 
        for row in reader:
            # csv has a header row, so we can use the column names as keys
            print(row['monsterName'])

def display_csv_pandas():
    df = pd.read_csv('./Week-7/Exercise Files/02/monsters.csv')
    # returns data frame, which is a table-like data structure
    print(df)

if __name__ == "__main__":
    pass
    # display_csv()
    # display_csv_dict()
    # display_csv_pandas()


# 2.5: Extract text from PDF files using Python

import PyPDF2

def display_pdf():
    # must use binary mode
    with open('./Week-7/Exercise Files/02/recipe-book.pdf', 'r+b') as f:
        reader = PyPDF2.PdfReader(f)
        print(len(reader.pages)) # number of pages
        print(reader.metadata) # document info (title, author, etc.
        page = reader.pages[1] # get page
        print(page.extract_text()) # extract text from page

if __name__ == "__main__":
    pass
    display_pdf()
