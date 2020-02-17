import os
import time
from tkinter import messagebox
from tkinter import Tk
import subprocess
from datetime import datetime
from sys import exit





class TimeKeeper:
    def __init__(self, path_to_file=None):
        self.__greet_text = "Plan your Work, Work your Plan!"
        self.__title = "Time Keeper"
        self.__work_session_duration = 1500
        self.__break_session_duration = 300
        self.__work_session_text = "Good Job! Take a break"
        self.__break_session_text = "Back to Work!"
        self.__work_sessions_total = 16
        self.__work_session_count = 1
        self.__want_to_work_text = "Do you wish to work today?"
        os.makedirs(os.path.join(os.path.join(os.path.expanduser(
            '~'), 'Documents'), 'task_keeper'), exist_ok=True)
        self.__path_to_file = os.path.join(os.path.join(
            os.path.expanduser('~'), 'Documents'), 'task_keeper')
        self.__file_name = "tasks_and_notes"
        self.__file_ext = ".md"
        self.__fully_qual_file_name = os.path.join(
            self.__path_to_file, (self.__file_name + self.__file_ext))

    def __day_greets(self):
        return messagebox.showinfo(self.__title, self.__greet_text)
    
    def __continue_dialog(self):
        return messagebox.askokcancel(self.__title, self.__want_to_work_text)

    def __file_calls(self):
        if os.path.exists(self.__fully_qual_file_name):
            print('file_calls')
            return subprocess.run(['start', self.__fully_qual_file_name], shell=True)
        subprocess.run(['echo', '', '>', self.__fully_qual_file_name], shell=True)
        return subprocess.run(['start', self.__fully_qual_file_name], shell=True)

    def __time_keeper(self):
        self.__sleep_time = self.__work_session_duration
        while self.__work_session_count <= self.__work_sessions_total:
            time.sleep(self.__sleep_time)
            if self.__sleep_time == self.__work_session_duration:
                self.__work_session_count += 1
                messagebox.showinfo(self.__title, self.__work_session_text)
                self.__file_calls()
                if self.__work_session_count % 4:
                    self.__sleep_time = self.__break_session_duration
                else:
                    self.__sleep_time = self.__break_session_duration * 3
            else:
                messagebox.showinfo(self.__title, self.__break_session_text)
                self.__sleep_time = self.__work_session_duration
        return 'ok'

    def start(self):
        root = Tk()
        root.withdraw()
        if self.__continue_dialog():
            self.__day_greets()
            self.__file_calls()
            self.__time_keeper()
        return exit(0)


if __name__ == "__main__":
    t = TimeKeeper()
    t.start()
