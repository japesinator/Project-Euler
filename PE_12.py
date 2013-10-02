#!/usr/bin/env python

import math

def triangle(n):
    for i in range(n):
        n += i
    return n

def factor_count(n):
    factors = 0
    for i in range(1, int(math.floor(math.sqrt(n)))):
        if n % i == 0:
            factors += 1
            if i ** 2 != n:
                factors += 1
    return factors

num = 0

while True:
    num += 1
    print str(num) + ":  " + str(triangle(num)) + ":  " + str(factor_count(triangle(num)))
    if factor_count(triangle(num)) > 500:
        break

print triangle(num)

