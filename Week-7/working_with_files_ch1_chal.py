import os
from pathlib import Path

# my method
def count_files_scandir(directory):
    count = 0
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                count += 1
                # print("File name:", entry.name)
            elif entry.is_dir():
                num = count_files_scandir(entry.path)
                count += num
    return count

# alternative method
def count_files_walk(directory):
    count = 0
    for dirpath, dirnames, files in os.walk(directory):
        for file in files:
            count += 1
    return count

# another alternative method
def count_file_path(directory):
    count = 0
    for entry in Path(directory).iterdir():
        if entry.is_file():
            count += 1
        elif entry.is_dir():
            num = count_file_path(entry)
            count += num
    return count

if __name__ == "__main__":
    # scandir option
    print(count_files_scandir('C:\\Users\\jayde\\Desktop'))
    # os.walk option
    print(count_files_walk('C:\\Users\\jayde\\Desktop'))
    # pathlib option
    print(count_file_path('C:\\Users\\jayde\\Desktop'))
