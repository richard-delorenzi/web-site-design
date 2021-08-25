#!/usr/bin/python3

import sys
import shutil
from os import listdir
from os.path import isfile, isdir, join

if len(sys.argv) == 3 :
    to_path=sys.argv[1]
    file=sys.argv[2]
else:
    to_path="a"
    file="test"

def do_copy(to_path,file):
    sub_dirs = [ dir+ "/" for dir in
                 [join(to_path, d) for d in listdir(to_path)]
                 if isdir(dir) ]

    for dir in sub_dirs:
        print ("copying: " +file+ " to " +dir)
        shutil.copy(file,dir)

do_copy(to_path, file)
