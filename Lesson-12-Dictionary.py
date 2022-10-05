#!/bin/python3
#coding: UTF8
#   {---------------Item----------------}
#   {--KEY--}    (--------VALUE---------)
enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Tergar',
    'image': ['healthy', 'sick', 'dead']
}

all_enemy = []  # создание массива для наполнения словарями
#for somebody in all_enemy:
#    print(somebody)            #  если производить вывод то он будет пустой, т.к. массив пустой

 # all_enemy.append(enemy)   #  наполнение(клонирование)  массива элементами
#all_enemy.append(enemy.copy())    # наполнение(генерация из исходного) массива элементами

for x in range(0, 5):      # добавление элемента - словаря, в массив, с использованием цикла
#    all_enemy.append(enemy)   #  наполнение(клонирование)  массива элементами
    all_enemy.append(enemy.copy())    # наполнение(генерация из исходного) массива элементами
    all_enemy[x]['name'] =  all_enemy[x]['name'] + str(x)
#print(all_enemy)

all_enemy[3]['health'] -= 10
all_enemy[2]['name'] = 'Tankar'
all_enemy[1]['color'] = 'yellow'

for somebody in all_enemy:
#    print(somebody['color'],somebody['health'])     # вывод нескольких ИТЕМОВ словаря
    print(somebody)     # вывод всех ИТЕМОВ словаря

print( 6 / 4)
print( 6 // 4)
print( 6 / -4)
print( 6 // -4)
