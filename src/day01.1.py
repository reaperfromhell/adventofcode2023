#!/usr/bin/python
# Python3 program to solve adventofcode.com/2023 

res = 0

with open("../input/day01.txt") as file_in:
    for line in file_in:
        numbers = ''.join(filter(str.isdigit, line))  #strip letters from line
        res = res + int(f"{numbers[0]}{numbers[-1]}") #add the first and last digit (if line only has one digit, it gets counted twice
print(res)