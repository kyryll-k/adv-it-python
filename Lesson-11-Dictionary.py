#!/bin/python3
#coding: UTF8
#   {------Item-------}
#   {KEY}    (VALUE)
enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Tergar',
}

enemy['rank'] = 'Leader'
#print(enemy)
del(enemy['rank'])
#print(enemy) 
#print ("Location:",enemy['loc_x'],enemy['loc_y'])

enemy['loc_x'] += 40
enemy['color'] = 'yellow'
#print(enemy)
print(enemy.keys())	#- вывод(печать) всех ключей словаря
print(enemy.values())	#- вывод(печать) всех значений словаря
print(enemy)

