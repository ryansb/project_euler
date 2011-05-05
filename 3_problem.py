#!/usr/bin/env python
# Author: Ryan Brown
# Description: 

tofactor = 600851475143
def primes():
	for n in range(2, 10000000):
		for x in range(2, n):
			if n % x == 0:
				break
			if(x==n-1):
				yield n
p = primes()
plist = []
factors = []
np = 2
while(tofactor != 1):
	np = p.next()
	while(tofactor%np==0):
		tofactor = tofactor/np
		factors.append(np)
print np
