#!/usr/bin/env python

from datetime import date
answer = 0

for year in range(1901, 2001):
  for month in range(1, 13):
    if date(year, month, 1).weekday() == 6:
      answer += 1

print answer
