#!/usr/bin/env python
import math

def amicable_test(n):
  def factor_sum(m):
    divisors = []
    for i in range(2, int(math.floor(math.sqrt(m)) + 1)):
      if m % i == 0:
        divisors.append(i)
        divisors.append(m/i)
    return sum(divisors) + 1
  if factor_sum(factor_sum(n)) == n and factor_sum(n) != n:
    return True
  else:
    return False

answer = 0

for i in range(2, 10000):
  if amicable_test(i) == True:
    answer += i

print answer
