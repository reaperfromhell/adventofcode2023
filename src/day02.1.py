#!/usr/bin/python
# Python3 program to solve adventofcode.com/2023 

res = 0
prep = { 'red': 12, 'green': 13, 'blue': 14 }

with open("../input/day02.txt") as file_in:
    for line in file_in:
        game = line.split(":")
        game_id = game[0].split()[1]
        possible = True
        for i in game[1].split(";"):
            for j in i.split(","):
                x = j.split()
                if int(x[0]) > prep[x[1]]:
                    possible = False
                    break
        if possible:
            res = res + int(game_id)
print(res)