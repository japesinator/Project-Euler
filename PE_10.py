#!/usr/bin/env python

import math
primes_found = []
i = 1

while True:
    i += 1
    if i == 2000000:

        break
    is_prime = True
    for j in primes_found:
        if j > math.sqrt(i):
            break
        elif i % j == 0:
            is_prime = False
            break
    if is_prime == True:
        primes_found.append(i)
        print str(len(primes_found)) + ":  " + str(i)

answer = 0

for i in primes_found:
    answer += i

print answer
