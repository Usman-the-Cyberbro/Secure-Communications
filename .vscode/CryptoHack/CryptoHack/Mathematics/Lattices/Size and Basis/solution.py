#!/usr/bin/python3

from math import sqrt

v = (4, 6, 2, 5)

size = 0

for i in v:
	size += pow(i,2) 

size = sqrt(size)

print(size) 