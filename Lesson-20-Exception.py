#!/bin/python3
#coding: UTF8
import sys, glob ,os
##os.chdir ("./")
dirf = "./files/"
_file = "lessons_list.tx"

#while True:
try:
    flist = dirf + _file
    rd_file = open(flist, mode='rt', encoding='utf-8')
except Exception:
    print(sys.exc_info()[1])
#        _file = input("Input new filename!: ")
else:
    print(rd_file.read())
#    sys.exit()

print("That's all folks!")
#finally:
#    print("Regardless of result Do something!")

#wr_file = open(flist, mode='w', encoding='utf-8')
#for file in glob.glob("Le*.py"):
#    wr_file.write (file)
#    new_line = "\n"
#    wr_file.write (new_line)
#wr_file.close()

