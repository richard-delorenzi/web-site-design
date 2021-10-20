#!/usr/bin/python3

import sys
import shutil
from os import listdir
from os.path import isfile, isdir, join

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

if len(sys.argv) == 3 :
    to_path=sys.argv[1]
    file=sys.argv[2]
else:
    self_name=sys.argv[0]
    eprint(f"error: Usage {self_name} to_path from_file")
    eprint(f"where to_path is a directory containing all the directories that you want the file in")
    eprint(f"and from_file is a file or directory")
    exit(-1)

def do_copy(to_path,file):
    sub_dirs = [ dir+ "/" for dir in
                 [join(to_path, d) for d in listdir(to_path)]
                 if isdir(dir) ]

    for dir in sub_dirs:
        print ("copying: " +file+ " to " +dir)
        shutil.copy(file,dir)

do_copy(to_path, file)
