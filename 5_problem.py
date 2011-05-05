#!/usr/bin/env python
# Author: Ryan Brown
# Description: 
maxi = 20
factors = range(1,maxi)
divisor=2
microfactors=[]
for maximum in factors:
	while True:
		if(divisor > maximum):
			break
		if(maximum%divisor == 0):
			maximum = maximum/divisor
			microfactors.append(divisor)
		if(maximum%divisor!=0):
			divisor = divisor + 1
print 
