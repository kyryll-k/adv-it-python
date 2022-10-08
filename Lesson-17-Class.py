#!/bin/python3
#coding: UTF8

from hero_cl import Hero_cl
from hero_cl import SHero_cl

hero1 = Hero_cl("Targar", 3, "Human")
hero1.show_hero()
hero1.level_up()
hero1.show_hero()
# print(type(hero1))

shero2 = SHero_cl("Sandro", 5,"Necro", 10)
shero2.show_hero()
shero2.cast()
shero2.show_hero()
shero2.__mlevel = 12
shero2.show_hero()