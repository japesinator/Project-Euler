#!/usr/bin/env python
answer = 0

def numCount(n):
  numArray = []
  # Make an array of digits for easy manipulation
  for i in str(n):
    numArray.append(int(i))
  # Define a function for regular last-digit number counting
  def lastDigit():
    global answer
    digit = numArray[-1]
    if digit == 1:   # one
      answer += 3
    elif digit == 2: # two
      answer += 3
    elif digit == 3: # three
      answer += 5
    elif digit == 4: # four
      answer += 4
    elif digit == 5: # five
      answer += 4
    elif digit == 6: # six
      answer += 3
    elif digit == 7: # seven
      answer += 5
    elif digit == 8: # eight
      answer += 5
    elif digit == 9: # nine
      answer += 4
    # If the last digit is zero, then it shouldn't matter unless it causes an 'and' to be ommitted, which is handled later

  if len(numArray) == 1:
    lastDigit()
  # If the number is of the form *1?, where * is any string and ? is any character, the written form is weird.  Thanks English language
  if len(numArray) >= 2:
    penDigit = numArray[-2]
  else:
    penDigit = "Lol"
  if penDigit == 1:
    global answer
    endDigit = numArray[-1]
    if endDigit == 1:   # eleven
      answer += 6
    elif endDigit == 2: # twelve
      answer += 6
    elif endDigit == 3: # thirteen
      answer += 8
    elif endDigit == 4: # fourteen
      answer += 8
    elif endDigit == 5: # fifteen
      answer += 7
    elif endDigit == 6: # sixteen
      answer += 7
    elif endDigit == 7: # seventeen
      answer += 9
    elif endDigit == 8: # eighteen
      answer += 8
    elif endDigit == 9: # nineteen
      answer += 8
    elif endDigit == 0: # ten
      answer += 3
  elif penDigit == 2:
    answer += 6 # twenty
    lastDigit()
  elif penDigit == 3:
    answer += 6 # thirty
    lastDigit()
  elif penDigit == 4:
    answer += 5  # forty
    lastDigit()
  elif penDigit == 5:
    answer += 5 # fifty
    lastDigit()
  elif penDigit == 6:
    answer += 5 # sixty
    lastDigit()
  elif penDigit == 7:
    answer += 7 # seventy
    lastDigit()
  elif penDigit == 8:
    answer += 6 # eighty
    lastDigit()
  elif penDigit == 9:
    answer += 6 # ninety
    lastDigit()
  elif penDigit == 0:
    lastDigit
  def firstDigit():
    digit = numArray[0]
    global answer
    if digit == 1:   # one
      answer += 3
    elif digit == 2: # two
      answer += 3
    elif digit == 3: # three
      answer += 5
    elif digit == 4: # four
      answer += 4
    elif digit == 5: # five
      answer += 4
    elif digit == 6: # six
      answer += 3
    elif digit == 7: # seven
      answer += 5
    elif digit == 8: # eight
      answer += 5
    elif digit == 9: # nine
      answer += 4
  if len(numArray) > 2:
    firstDigit()
    if numArray[-1] != 0 or numArray[-2] != 0:
      answer += 3 # and
    answer += 7   # hundred

for i in range(1, 1000):
  numCount(i)
answer += 11 # one thousand
print answer
