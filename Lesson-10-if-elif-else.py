#!/bin/python3


#a = range(1,10,2) 
#b = range(10,1,-1)
#c = "****    $$$$$___DDD***DDD____$$$$$    *****"
#print(c.strip("*$_ "))

#for age in range (-10,0,2):
#    print(f"---Num-- {age}")

#while True:
#    age+=1 ; print(age)

#cities = [ 'New York', 'Kyiv', 'Lviv']
#print(cities)
#cities.sort(reverse=True)
#print(cities)
car=input()

all_cars = ['honda','toyota','bmv', 'vw', 'seat', 'skoda', 'tesla'] 
german_cars = ['bmv', 'vw', 'seat', 'skoda'] 

if car in all_cars:
    print ("It's a good car!")
else:
    print ("Is it a bucket?")

print("======")

for car in all_cars:
    if car in german_cars:
        print (car.upper(), "is a good german car!")
    else:
        print(car.lower(),"isn't a german! (")
