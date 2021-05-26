__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil
from zipfile import ZipFile
cwd = os.getcwd()
zip_file_path = os.path.join(cwd,"data.zip") 
cache_dir_path = os.path.join(cwd,"cache")
current_folder = os.getcwd()

def clean_cache():
    cache_path = os.path.join(current_folder, "cache")
    if 'cache' in os.listdir(os.getcwd()):
        shutil.rmtree(cache_path)
    if 'cache' not in os.listdir(os.getcwd()):
        os.mkdir('cache')

        
def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path, 'r') as zip:
        zip.extractall(cache_dir_path)


def cached_files():
    cached_files_list = []
    cached_files_info = list(os.walk(cache_dir_path))
    for file in (cached_files_info[0][2]):
        file_path = os.path.join(current_folder, "cache", file)
        cached_files_list.append(file_path)
    return cached_files_list
cached_files = (cached_files())


def find_password(cached_files):
    for file_name in cached_files:
        with open(file_name, "r") as file:
            for line in file:
                if "password" in line:
                    password_line = line.split(": ")[1]
    return password_line


if __name__ == "__main__":
    print(clean_cache())
    print (cache_zip(zip_file_path, cache_dir_path))
    print(f'The password is: {find_password(cached_files)}')
