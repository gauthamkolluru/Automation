import os
import sys
import subprocess

DIRECTORIES = ('Desktop', 'Documents', 'Downloads')
FILE_TYPES = ('md', 'docx', 'xlsx', 'txt')


# take the 'Search Directory' as 'CWD' by default if current user's 'Home' is in the path

def search_path_list():
    return [os.path.join(os.path.expanduser('~'), directory) for directory in os.listdir(os.path.expanduser('~')) if directory in DIRECTORIES]


def search_string_func():
    return ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else input('Enter Search String: ')


def find_files():
    search_string = search_string_func()
    file_name_list = []
    for search_path in search_path_list():
        for root, directories, files in os.walk(search_path):
            for f in files:
                file_name = os.path.join(root, f)
                if file_name.split('.')[-1] in FILE_TYPES:
                    try:
                        with open(file_name, 'r') as fn:
                            if search_string.lower() in fn.read().lower():
                                file_name_list.append(file_name)
                    except Exception as e:
                        pass
                        # print('error in file: ', file_name, repr(e))
    return file_name_list


files_list = find_files()

for each_file in files_list:
    if input("Do you want to open {} ? (y/n)".format(os.path.split(each_file)[-1])).lower() != 'n':
        subprocess.run(['start', each_file], shell=True)
