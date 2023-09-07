from pathlib import Path
from datetime import datetime

def get_creation_date(path):
    stats = path.stat()
    creation_date = stats.st_ctime
    utc_timestamp = datetime.utcfromtimestamp(creation_date)
    return utc_timestamp.strftime('%Y-%m-%d')

def rename_files(image_folder):
    files_types = ['.png', '.svg']
    for path in Path(image_folder).iterdir():
        if path.is_file() and path.suffix in files_types:
            date = get_creation_date(path)
            new_path = Path(image_folder+'/'+date+path.stem+path.suffix)
            path.rename(new_path)

if __name__ == "__main__":
    rename_files('Week-7/Exercise Files/03/chal_images/')