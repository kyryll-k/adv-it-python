#!/bin/python3
#coding: UTF8
import time

#import loguru
#from loguru import logger
#logger.add('/Users/kk/github/adv-it-python/logs.log', level='DEBUG')
#logger.debug('Error')
#logger.info('Information message')
#logger.warning('Warning')

# name = str(input("Input your name: "))
# print ("Your name is: ",name)

# X = int(input("Input X: "))
# Y = int(input("Input Y: "))
# Z = X + Y ; print (Z)

print(time.perf_counter())
history = []

pswd = ""
while pswd != 'sekret' :
    history.append (pswd)
    pswd = input (pswd + " : is Wrong password. Input new! \n ")


print ("Password accepted! You will be destroyed in: ")
for x in range (3,0,-1):
    print (x)
    time.sleep(1)

print ("    <M>") 
print ("  <<MMM>>")
print ("<<<!BOOM!>>>")
print ("  <<VVV>>")
print ("    <V>")


print (history)

print(time.perf_counter())