#!/usr/bin/python
# Python3 program to solve adventofcode.com/2023 

res = 0
numbers_dict = { 'one':"1", 'two':"2", 'three':"3", 'four':"4", 'five':"5", 'six':"6", 'seven':"7", 'eight':"8", 'nine':"9"}


with open("../input/day01.txt") as file_in:
    for line in file_in:
        numbers = ""
        for i, x in enumerate(line.strip()):
            if x.isdigit():
                numbers = numbers + x
                continue
            for j in range(i+2, i+6):
                if line[i:j] in numbers_dict:
                    numbers = numbers + numbers_dict[line[i:j]]
        res = res + int(numbers[0]+numbers[-1]) #add the first and last digit (if line only has one digit, it gets counted twice)
print(res)