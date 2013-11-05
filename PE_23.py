#!/usr/bin/env python

from math import *

def factor_sum(n):
  return_value = 1
  for i in range(2, int(floor(sqrt(n)))+1):
    if n % i == 0:
      return_value += i
      return_value += n / i
  if floor(sqrt(n)) == sqrt(n):
    return_value -= int(sqrt(n))
  return return_value  

def abundant_sum_test(n):
  if n >= 48 and n % 2 == 0:
    return True
  for i in range(int(floor(len(abundant_numbers) / 2) + 1)):
    for j in range(i, len(abundant_numbers)):
      if abundant_numbers[i] + abundant_numbers[j] == n:
        return False
  else:
    return True

answer = 1  
abundant_numbers = []

for i in range(2, 21612):
  print i          
  if abundant_sum_test(i) == False:
    answer += i
  if factor_sum(i) > i:         
    abundant_numbers.append(i)

print answer
print abundant_numbers
print 
