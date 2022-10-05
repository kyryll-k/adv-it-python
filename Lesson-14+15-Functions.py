#!/bin/python3
#coding: UTF8
import time
print(time.perf_counter())

#WHO = "Alex"  HOW = "Welthy" AGE = 66

##def happy(WHO, HOW):
##    print("Dear " + WHO + "! " + "I wish you be " + HOW)
##happy ("Kyrylo", "Healthy")

###def RETURN (x,y,z):
###    return x+y+z

###S = RETURN (1,2,3)
###print(S)

def fct(x):     # создание функции факториала
    val = 1
    for i in range (1, x+1):    # x+1 используется для создания ренджа включающего значения входной переменной
        val *=i             # *= краткая запись умножения переменной на число 
    return val

print(fct(5))

def dict_creating(fname, lname, date):
    record = { 
        'name': fname,
        'surname': lname,
        'date': date }
    return record

customer1 = dict_creating("Jonh","Tolkien","1905")
customer2 = dict_creating("Arthur","Doule","1895")

print (customer1)
print (customer2)

def award(virtu , *persons):
    for person in persons:
        print ( virtu, person )

award("Otvaga", "Sania", "Lexa")