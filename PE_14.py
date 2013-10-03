#!/usr/bin/env python

def collatz(n):
    steps = 0
    while True:
	if n == 1:
	    break
	elif n % 2 == 0:
	    n /= 2
	    steps += 1
	else:
	    n *= 3
	    n += 1
    return steps

answer = 0
max_steps = 0

for i in range(1, 1000001):
    if collatz(i) > max_steps:
	max_steps = collatz(i)
	answer = i

print answer

