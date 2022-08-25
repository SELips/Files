__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


from os import listdir
import os
from os.path import isfile, join
import shutil

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'cache')
data_zip = os.path.join(current_directory, 'data.zip')

def clean_cache():
    if os.path.exists(final_directory):
        shutil.rmtree(final_directory)
    os.makedirs(final_directory)

def cache_zip(zip_file_path, cache_path):
    return shutil.unpack_archive(zip_file_path, cache_path)


def cached_files():
    all_cache_files = []
    # current_directory = os.getcwd()
    # current_files = os.path.abspath(join(current_directory, "cache"))
    for file in listdir(final_directory):
        full_path = join(final_directory, file)
        if isfile(full_path):
            all_cache_files.append(full_path)
    return all_cache_files


def find_password(full_path):
    full_path = cached_files()
    for file in full_path:
        with open(file, 'r') as f:
            lines = f.readlines()
            for words in lines:
                if 'password' in words:
                    final_password = words.split(" ")
                    final_password = final_password[1].split("\n")
                    return final_password[0]


if __name__ == "__main__":
    # clean_cache()
    # cache_zip(data_zip,current_directory)
    # cached_files()
    find_password(final_directory)
