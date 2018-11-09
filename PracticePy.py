#!/usr/bin/env python

numStars = 1
numSpaces = 5
i = 0
j = 0

for h in range(0, 5):
    for i in range(0, numSpaces):
        print(" ", end = " ")

    for j in range(0, numStars):
        print("*", end = " "),

    print("\n", end = " ")
    numSpaces = numSpaces - 1
    numStars = numStars + 1

print("ENd", end = " ")
