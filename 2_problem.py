#!/usr/bin/env python
# Author: Ryan Brown
# Description: 
def fibonacci():
	"""a generator for Fibonacci numbers, goes to next number in series on each call"""
	a, b = 1, 2
	while True:
		yield a
		a, b = b, a + b

f = fibonacci()
fibs = []
while(1):
	fi = f.next()
	if(fi < 4000000):
		fibs.append(fi)
	else:
		break
evens = []
for f in fibs:
	if(f%2==0):
		evens.append(f)

print sum(evens)
