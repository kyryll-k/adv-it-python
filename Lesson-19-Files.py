#!/bin/python3
#coding: UTF8
#import os

inputuser = "./files/user_names.txt"
inputpass = "./files/list_of_passwords.txt"
outpass = "./files/finded_passwords.txt"
# inputfile = "/Users/kk/github/adv-it-python/files/user_names.txt"

myusers = open(inputuser, mode='r', encoding='utf-8')
mypasses = open(inputpass, mode='r', encoding='utf-8')
findpass = open(outpass, mode='wt')
# findpass = open(outpass, mode='at')
#print(myfile.read())

#for line in myfile:
#    print("Hello " + line)

passfind = input("What pass we need to find? ")

for num, line in enumerate(myusers, 1):
    if "Kinley" in line:
        print("Line №: " + str(num) + " " + line)

for num, line in enumerate(mypasses, 1):
    if passfind in line:
        print("Line №: " + str(num) + " " + line)
        findpass.write(line)

inputuser.close()
inputpass.close()
outpass.close()