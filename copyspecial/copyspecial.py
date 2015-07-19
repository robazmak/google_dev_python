#!/usr/bin/python3 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise"""


def get_special_paths(directory):
    files = os.listdir(directory)
    special_files = [name for name in files if re.search(r'__\w+__', name)]
    abs_path_files = []
    for name in special_files:
        path = os.path.join(directory, name)
        abs_path_files.append(os.path.abspath(path))
    return abs_path_files


def copy_to(paths, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        for path in paths:
            shutil.copy(path, directory)
    else:
        print(directory, 'already exists. Quitting.')


def zip_to(paths, zippath):
    print("Command I'm going to do: zip -j", zippath, paths)
    try:
        subprocess.call(['zip', '-j', zippath] + paths)
    except IOError:
        sys.strerr.write('Error in zipping:', zippath)
        sys.exit(1)


def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]
        copy_to(get_special_paths(args[0]), todir)
        sys.exit(0)

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]
        zip_to(get_special_paths(args[0]), tozip)
        sys.exit(0)

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)
    else:
        files = get_special_paths(args[0])
        for filename in files:
            print(filename)

if __name__ == "__main__":
    main()
