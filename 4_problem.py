#!/usr/bin/env python
# Author: Ryan Brown
# Description: 
import itertools
palin = []
three_digits = range(100,999)
for pair in list(itertools.permutations(three_digits, 2)):
	pal = pair[0] * pair[1]
	if(str(pal)==str(pal)[::-1]):
		palin.append(pal)
palin.sort()
print palin
