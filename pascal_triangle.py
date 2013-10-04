#!/usr/bin/env python

def pascal_triangle(n):
  if n == 1:
    return [1]
  else:
    newline = [1]
    for i, j in pascal_triangle(n-1):
      if i != 0:
        newline.append(j + pascal_triangle(n-1)[i-1]
    newline.append(1)
    return newline

print pascal_triangle(1)
print pascal_triangle(2)
print pascal_triangle(3)
