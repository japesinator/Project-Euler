#!/usr/bin/env python

import math

def paths(x,y):
  return math.factorial(x + y) / (math.factorial(x) * math.factorial(y))

print paths(20, 20)
