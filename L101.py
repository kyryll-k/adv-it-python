#!/bin/python3
#coding: UTF8

import sys, glob # , os
##os.chdir ("./")
dirf = "./files/"
_file = "lessons_list.txt"
writefile = dirf + _file



flist = open(writefile, mode='w', encoding='utf-8')
# flist.truncate()
for file in glob.glob("Le*.py"):
    flist.write (file)
    new_line = "\n"
    flist.write (new_line)
flist.close()     
