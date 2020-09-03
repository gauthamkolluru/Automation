import os
import json

import subprocess


FILE_NAME = "pdf_passwords.json"


def read_json(file_name: str, data=dict()) -> (str, list):

    with open(file_name) as fn:
        data = json.load(fn)

    return data['root_dir'], data['passwords']


root_dir, PASSWORDS = read_json(FILE_NAME)


def get_files(directory=root_dir) -> str:

    if os.path.exists(directory):

        for f in os.listdir(directory):
            yield os.path.join(directory, f)


def get_password() -> str:

    for v in PASSWORDS:
        yield v


def subprocess_args(file_name: str, password: str) -> list:

    return ['qpdf', "--decrypt", "--password={}".format(password), "--replace-input", file_name]


def pdf_rm_pwd() -> bool:

    for f in get_files():

        if f.endswith(".pdf"):

            for password in get_password():

                output = subprocess.run(subprocess_args(
                    f, password), capture_output=True)

                if not output.returncode:
                    break
    return True


def main():

    return pdf_rm_pwd()


if __name__ == '__main__':

    if main():

        print("Process Completed")
