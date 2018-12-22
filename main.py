import sys
import os
import shutil
import re

EXTS = ['mp4', 'mkv', 'avi']

def panic(msg):
    print('Panic: ' + msg)
    exit(1)

def getext(path):
    return path.split('.')[-1]

def clean(path):
    ext = getext(path)
    result = re.search('[sS][0-9]+[eE][0-9]+', path)
    return result.group(0).upper() + '.' + ext

if len(sys.argv) < 2:
	path = '.'
else:
	path = sys.argv[1]
	
if not os.path.isdir(path):
    panic(path + ' is not a directory')

files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
files = [f for f in files if getext(f) in EXTS]

for f in files:
    cleaned = clean(f)
    shutil.move(f, cleaned)

