#!/usr/bin/env python

units = ["", "one", "two", "three", "four",  "five", "six", "seven", "eight", "nine"]
teens = ["", "eleven", "twelve", "thirteen",  "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty","fifty", "sixty", "seventy", "eighty", "ninety"]

def word_length(n):
    
    answer = 0
    
    char_array = []
    for i in str(n):
        char_array.append(int(i))
    
    if len(char_array) == 1:
        answer += len(units[n])
    
    else:
        if char_array[-2] == 1 and char_array[-1] != 0:
            answer += len(teens[char_array[-1]])
        else:
            answer += len(tens[char_array[-2]])
            answer += len(units[char_array[-1]])
    
    if len(char_array) > 2:
        answer += len(units[char_array[0]])
        answer += len('hundred')
        if char_array[1] != 0 or char_array[2] != 0:
            answer += len('and')
            
    return answer


final_answer = 0
for i in range(1, 1000):
    final_answer += word_length(i)
final_answer += len("onethousand")

print final_answer
