#!/bin/python3
#coding: UTF8

class Hero_cl(object):
    """Description of class hero characteristic"""

    def __init__(self, name, level, race):
        """Desc method"""
        self.name = name
        self.level = level
        self.race = race

    def show_hero(self):
        """show status hero"""
        message = (self.name + " Level is: " + str(self.level) + ". He is a " + self.race)
        print (message)
    
    def level_up(self):
        """Up level"""
        self.level += 1

class SHero_cl(Hero_cl):
    """CLass for super-hero"""
    def __init__(self,name, level, race, mlevel):
        """ Creatintg Shero"""
        super().__init__(name,level,race)
        self.__mlevel = mlevel
        self.magic = 100

    def cast (self):
        self.magic -= 10
        print (self.name + " cast spell!")

    def show_hero(self):
        """show status Shero"""
        message = (self.name + " Level is: " + str(self.level) + ". He is a " + self.race + ". Magic is: " + str(self.magic) + " " + str(self.__mlevel))
        print (message)
