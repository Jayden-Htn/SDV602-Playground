# Following the Linkedin course: Working with Files (2021) by Kathryn Hodge.
# I have used Python's file system before, but this will be much more in-depth then my current knowkedge.


# <---- 4: Working with Archives and Temporary Files  ---->

# 4.1:

# import zipfile
# import shutil # shutil is good for collections of files

def create_zip(files):
    # can do append as well
    with zipfile.ZipFile('./Week-7/Exercise Files/04/zipfile.zip', 'w') as z:
        for file in files:
            z.write(file) # copies file to zip

def created_nested_zip(dir_path):
    # creates a zip of the directory and all its contents
    shutil.make_archive('./Week-7/Exercise Files/04/nested_zip', 'zip', dir_path)

if __name__ == "__main__":
    files = [
        './Week-7/Exercise Files/04/monster01.png',
        './Week-7/Exercise Files/04/monster02.png',
        './Week-7/Exercise Files/04/monster03.png'
    ]
    # note path is included in zip
    # create_zip('./Week-7/Exercise Files/04/monster03.png')
    # created_nested_zip('./Week-7/Exercise Files/04/04_01/begin/')


# 4.2: Read from and extract ZIP archives

import zipfile

def read_zip():
    with zipfile.ZipFile('./Week-7/Exercise Files/04/zipfile.zip', 'r') as z:
        print(z.namelist()) # returns list of files in zip

def retrieve_zip_file_info():
    with zipfile.ZipFile('./Week-7/Exercise Files/04/zipfile2.zip', 'r') as z:
        file_info = z.getinfo('zipfile2/monster01.png')
        print(file_info)

def read_file_in_zip():
    with zipfile.ZipFile('./Week-7/Exercise Files/04/Archive.zip', 'r') as z:
        with z.open('description01.txt') as f:
            print(f.read())

def extract_file(archive, file_to_extract):
    with zipfile.ZipFile(archive, 'r') as z:
        z.extract(file_to_extract, './Week-7/Exercise Files/04/extracted/')

def extract_all():
    with zipfile.ZipFile('./Week-7/Exercise Files/04/Archive.zip', 'r') as z:
        z.extractall('./Week-7/Exercise Files/04/extracted/')

if __name__ == "__main__":
    pass
    # read_zip()
    # retrieve_zip_file_info()
    # read_file_in_zip()
    # extract_file('./Week-7/Exercise Files/04/Archive.zip', 'description01.txt')
    # extract_all()


# 4.3: Open and read TAR archives

# tar = Tape Archive

# import tarfile

def read_tar():
    # r:gz = open type and compression type
    # gz = gzip, bz2 = bzip2, xz = xz
    with tarfile.open('./Week-7/Exercise Files/04/archive.tar.gz', 'r:gz') as t:
        # print(t.getnames())
        # file = t.getmember('descriptions/description01.txt')
        for member in t.getmembers():
            print('---------------------')
            print('File name:', member.name)
            print('File size:', member.size)
            print('File mode:', member.mode)
    
def read_file_in_tar():
    with tarfile.open('./Week-7/Exercise Files/04/archive.tar.gz', 'r:gz') as t:
        # extract file returns a file object for reading and writing
        # temporary file, doesn't actually extract the file
        with t.extractfile('descriptions/description01.txt') as file:
            print(file.read())

if __name__ == "__main__":
    pass
    # read_tar()
    # read_file_in_tar()


# 4.4: Extract from and write to TAR archives

import tarfile

def create_tar_archive():
    # can add compression type
    files = ['monsters.csv', 
             'Monster_contact_sheet.pdf']
    with tarfile.open('./Week-7/Exercise Files/04/archive.tar', 'w') as t:
        for file in files:
            t.add(file)

def add_to_tar_archive():
    # append doesn't work for compressed files (7/2021)
    with tarfile.open('./Week-7/Exercise Files/04/archive.tar', 'a') as t:
        t.add('./Week-7/Exercise Files/04/monsters.csv')

def extract_tar():
    with tarfile.open('./Week-7/Exercise Files/04/archive.tar', 'r') as t:
        t.extract('monsters.csv', './Week-7/Exercise Files/04/')
        # what file, where to extract

def extract_all_tar():
    with tarfile.open('./Week-7/Exercise Files/04/archive.tar', 'r') as t:
        t.extractall('./Week-7/Exercise Files/04/')

if __name__ == "__main__":
    pass
    # create_tar_archive()
    # add_to_tar_archive()
    # extract_tar()
    # extract_all_tar()


# 4.5: Working with temporary files in Python

# handy as a quick backup or storage for an intermediate state

import tempfile

def work_with_temp_file():
    # file is automatically deleted when closed
    with tempfile.TemporaryFile('w+') as tf:
        tf.write('Id 5, Name: Bob')
        tf.seek(0) # go back to beginning of file
        print(tf.read())
        print(tempfile.gettempdir()) # get temp directory

if __name__ == "__main__":
    pass
    work_with_temp_file()

    

