#!/usr/bin/env python

factorial = 1

for i in range(2, 101):
  factorial *= i

answer = 0
for i in str(factorial):
  answer += int(i)

print answer
