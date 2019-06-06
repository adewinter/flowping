#!/usr/bin/python3

# -*- coding: utf-8 -*-

from zenipy import entry
import os
import datetime

user = 'adewinter'
home_dir = os.path.join('/', 'home', user)
data_dir = os.path.join(home_dir, '.flowping')


def get_placeholder_from_line(line):
    fields = line.split(',')
    if(fields.__len__() > 0):
        return fields[-1].strip()
    else:
        return ''


def start():
    try:
        # Create target Directory
        os.mkdir(data_dir)
        print("Directory", data_dir, "Created.")
    except FileExistsError:
        pass

    file_path = os.path.join(data_dir, 'data.csv')
    if not (os.path.exists(file_path)):
        f = open(file_path, 'w')
        f.close()

    read_file = open(file_path, 'r+')
    lines = read_file.readlines()
    if (lines.__len__() == 0):
        placeholder = 'Taking over the world'
    else:
        placeholder = get_placeholder_from_line(lines[-1])
    read_file.close()

    append_file = open(file_path, 'a+')
    result = entry(text="What are you working on?", placeholder=placeholder)
    now = datetime.datetime.now()

    data_to_append = f"{now},{result}\n"

    print(f"Appending {data_to_append} to datefile: {file_path}.")

    append_file.write(data_to_append)
    append_file.close()


if __name__ == "__main__":
    start()
