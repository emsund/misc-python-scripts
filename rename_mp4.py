#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, shutil 

# Feb 19, 2017
# Author: emsund

''' Copy *.mp4 files in a directory to a new dir, with a cropped filename. '''


li = os.listdir()
destdir = 'renamed'

# Make a folder to store the copies of renamed files
try:
    os.mkdir(destdir)
except FileExistsError:
    print('Directory "renamed" already exists. Using existing.')

for filename in li:
    splitname = filename.split('.')
    if splitname[-1] == "mp4":
        newname = splitname[0].split(';')[0] + '.mp4'
        print(newname)
        shutil.copy2(filename,destdir+'/'+newname)


