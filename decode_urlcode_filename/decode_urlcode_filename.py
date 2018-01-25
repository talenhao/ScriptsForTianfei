#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import os
import urllib.parse


def convert_filename(files):
    for file in files:
        unquote_file_name = urllib.parse.unquote(file)
        os.rename(file, unquote_file_name)


if __name__ == '__main__':
    files = os.listdir()
    convert_filename(files)