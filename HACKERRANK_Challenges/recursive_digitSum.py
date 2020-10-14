#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    len_num = len(n)
    if len_num != 1:
        digit_sum = 0
        for elem in n: #for every digit (element) in n
        #calculate the superdigit that is equal to the super digit of the sum of the digits of x.
            digit_sum += int(elem)
        str_sum = str(digit_sum*k) #doing the k times concatenation of the string
        return superDigit(str_sum,1) #call the recursion in case that there is more than 1 digit left
    elif len_num == 1: #otherwise, If x has only 1 digit (so the len is 1), then the super digit is x itself.
        return int(n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()
