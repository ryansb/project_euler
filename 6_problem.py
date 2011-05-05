#!/usr/bin/env python
# Author; Ryan Brown
# Description; Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

naturals = range(1,101)
print naturals
squaresum = 0
for i in naturals;
	squaresum+=i*i
print sum(naturals)*sum(naturals) - squaresum
