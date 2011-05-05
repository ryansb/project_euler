#!/usr/bin/env python
# Author: Ryan Brown
# Description: 
nat_nums = set()
for i in range(0,1000):
	if(i % 3 == 0):
		nat_nums.add(i)
	if(i % 5 == 0):
		nat_nums.add(i)
print sum(nat_nums)
