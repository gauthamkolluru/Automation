import os
import sys
import subprocess

DIRECTORIES = ('Desktop', 'Documents', 'Downloads')
FILE_TYPES = ('md', 'docx', 'xlsx', 'txt', 'py')


# take the 'Search Directory' as 'CWD' by default if current user's 'Home' is in the path

def search_path_list():
    return [os.path.join(os.path.expanduser('~'), directory) for directory in os.listdir(os.path.expanduser('~')) if directory in DIRECTORIES]


def search_string_func():
    return ' '.join([i for i in sys.argv[1:] if "C:".casefold() not in i.casefold() or "/" != i[0]]) if len(sys.argv) > 1 else input('Enter Search String: ')


def find_files(search_path_list=None, search_string=""):
    # search_string = search_string_func()
    file_name_list = []
    for search_path in search_path_list:
        for root, directories, files in os.walk(search_path):
            # print("printing : ", root, directories, files)
            for f in files:
                file_name = os.path.join(root, f)
                # print("printing filename", file_name)
                if file_name.split('.')[-1] in FILE_TYPES:
                    try:
                        with open(file_name, 'r') as fn:
                            # print("printing opened filename", file_name)
                            if search_string.casefold() in fn.read().casefold():
                                print("printing search string", search_string)
                                file_name_list.append(file_name)
                    except Exception as e:
                        pass
    return file_name_list


def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if os.path.expanduser('~').casefold() in arg:
                search_path_list = [arg]
            else:
                search_string = arg
    print(search_path_list, search_string)
    if not search_path_list:
        search_path_list = search_path_list().extend(os.path.abspath(os.curdir))
    if not search_string:
        search_string = input("Enter a string: ")

    files_list = find_files(
        search_path_list=search_path_list, search_string=search_string)

    print(files_list)

    for each_file in files_list:
        if input("Do you want to open {} ? (y/n)".format(os.path.split(each_file)[-1])).lower() in ['y', 'yes']:
            subprocess.run(['start', each_file], shell=True)


if __name__ == "__main__":
    main()
