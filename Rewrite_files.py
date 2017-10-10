#!/usr/bin/python

from sys import argv

script, name, age, birthmonth = argv

target = open("customers.txt", 'a')
target.write(name + "\n" + age + "\n" + birthmonth + "\n")
target.close()
print name, age, birthmonth
