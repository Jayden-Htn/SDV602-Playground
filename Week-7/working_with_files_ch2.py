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
    print_content()
    print("------------")
    write_content()
    print_content()



