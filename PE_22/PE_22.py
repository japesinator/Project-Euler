#!/usr/bin/env python

import csv
names_list = []
with open('names.txt', 'rb') as csvfile:
  csvnames = csv.reader(csvfile, delimiter=',', quotechar='"')
  for row in csvnames:
    for item in row:
      names_list.append(item)
names_list.sort()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
answer = 0

for index, name in enumerate(names_list):
  pre_answer = 0
  for name_letter in name:
    for letter_value, alphabet_letter in enumerate(alphabet):
      if name_letter == alphabet_letter:
        pre_answer += (letter_value + 1)
        break
  pre_answer *= (index + 1)
  answer += pre_answer

print answer
