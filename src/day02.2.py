#!/usr/bin/python
# Python3 program to solve adventofcode.com/2023 

res = 0

with open("../input/day02.txt") as file_in:
    for line in file_in:
        game = line.split(":")
        powers = { 'red': 0, 'green': 0, 'blue': 0 }
        for i in game[1].split(";"):
            for j in i.split(","):
                x = j.split()
                if int(x[0]) > powers[x[1]]:
                    powers[x[1]] = int(x[0])
        power = 1
        for z in powers.values():
            power = power * z
        res = res + power
print(res)