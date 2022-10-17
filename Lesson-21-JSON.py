#!/bin/python3
#coding: UTF8
import json, sys, glob ,os
##os.chdir ("./")

filename = "./files/user_settings.txt"
myfile = open(filename, mode='w', encoding='utf-8')
player1 = {                     # создание словаря параметров игрока
    'PlayerName': 'Donald',
    'Score': 145,
    'Awards': ['OR', 'NV', 'NY']
}
player2 = {                      # создание словаря параметров игрока
    'PlayerName': 'Mikkie',
    'Score': 245,
    'Awards': ['OH', 'VS', 'FR']
}

myplayers = []                 # создание пустого массива
myplayers.append(player1)      # добавление значения словаря в массив 
myplayers.append(player2)

json.dump(myplayers, myfile)

myfile.close()

myfile = open(filename, mode='r', encoding='utf-8')
json_load = json.load(myfile)

print(json_load)

for user in json_load:
    print("Player is: " + str(user['PlayerName']))
    print("Score is: " + str(user['Score']))
    print("Awards is: " + str(user['Awards']))