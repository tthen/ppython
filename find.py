# How to use glob() to find files recursively?
# https://stackoverflow.com/questions/2186525/how-to-use-glob-to-find-files-recursively

import os, fnmatch


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


for filename in find_files('docspdf', '*bootstrap*.pdf'):
    print ('Found pdf files:', filename)
