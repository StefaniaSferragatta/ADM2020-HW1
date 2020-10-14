import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
if (n>0 and m>0 and n<100 and m< 100):
    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    for _ in range(m):
        string = ""
    for cols in range (m):
        for rows in range (n):
            string += matrix[rows][cols]
    output = re.sub(r"\b[!@#$%& ]+\b"," ", string)
    print(output)
