import os, random
import pathlib

import random,os
import re

#DEV: do extention filter
def fetchNote(directory):
    files = os.listdir(directory)
    file = random.choice(files)
    return directory + '/' + file


def fetchNote2(directory):
    pattern = '.*\.txt|.*\.md' #files with certain extension
    matches = []

    for path, subdirs, files in os.walk(directory):
        for name in files:
            if re.match(pattern, name):
                matches.append(os.path.join(path,name))

    return random.choice(matches)
