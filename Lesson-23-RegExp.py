#!/bin/python3
#coding: UTF8
import re

mytext = "Oleksandr - 1982 - 1982198219 - Male - ol@r.com" \
         "Mykolay - 1954 - 1954195419 - Male - my@y.com" \
         "Galyna - 1985 - 1985198519 - Female - ga@a.com" \
         "Petro - 1945 - 1945194519 - Male - pe@o.com" \
         "Kyrylo - 1980 - 1980198019 - Male - ky@o.com" \
         "Vasyl - 1979 - 1979197919 - Male - va@l.com" \
         "Dmytro - 1961 - 1961196119 - Male - dm@o.com" \
         "Maryna - 1969 - 1961196119 - Female - ma@a.com"

#textlookfor = r"\d..."    # поиск первого символа цифры
#textlookfor = r"\D..."    # поиск первого символа не цифры
#textlookfor = r"\w..."    # поиск первого символа алфавита и/или цифры 
#textlookfor = r"\W..."    # поиск первого символа не алфавита и/или цифры 
#textlookfor = r"\s[0-9]{10}\s"  # поиск пробела,десяти символов из 0-9, и заканчивающегося пробелом
# в фигурных скобках указываеться количество символов указанных в квадратных скобках
textlookfor = r"[A-Z][a-z]+\s"
allresults = re.findall(textlookfor, mytext)

print(allresults)