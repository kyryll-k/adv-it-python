#!/bin/python3
#coding: UTF8
import re

inputfile = "./files/randata.txt"
resultfile =  "./files/results.txt"

inpf = open(inputfile, mode='rt', encoding='utf-8')
outf = open(resultfile, mode='w', encoding='utf-8')
data = inpf.read()

findnext = r"[A-Za-z0-9-.]+@(?!yahoo)(?!google)[A-Za-z0-9-.]+\.[A-Za-z-]+"
results = re.findall(findnext, data)

for item in results:
    outf.write(item + str("\n"))
print("Total count is: " + str(len(results)))

inpf.close() ; outf.close()