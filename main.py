__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


#Hallo WINC-nakijker! Ik had alles op groen maar doordat ik op mijn werklaptop werk en ik soms random admin-fouten krijg dat ik ergens niet bij kan door de vpn. 
#Deed mijn code opeens weer vreemd. Ik stuur hem nu gewoon op in de hoop dat het bij jullie wel in één keer lukt. Thanks voor het nakijken.  


from os import listdir
import os
from os.path import isfile, join
import shutil

def clean_cache():
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'cache')
    if os.path.exists(final_directory):
        shutil.rmtree(final_directory)
    os.makedirs(final_directory)
clean_cache()

def cache_zip(zip_file_path, cache_path):
    return shutil.unpack_archive(zip_file_path, cache_path)
cache_zip('./data.zip','./cache')

def cached_files():
    all_cache_files = []
    current_directory = os.getcwd()
    current_files = os.path.abspath(join(current_directory, "cache"))
    for file in listdir(current_files):
        full_path = join(current_files, file)
        if isfile(full_path):
            all_cache_files.append(full_path)
    return all_cache_files
cached_files()


def find_password(full_path):
    full_path = cached_files()
    for file in full_path:
        with open(file, 'r') as f:
            lines = f.readlines()
            for words in lines:
                if 'password' in words:
                    final_password = words.strip("\n")
                    final_password = words.strip("password: ")
                    return final_password
print(find_password('//REMOTE.aequator.nl/UserFolders/selips/Documents/Administratie/WINC - Data analytics full course/files/cache'))