#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    tot_likes = 0
    people_shared = 5
    while (n!=0):
        like = people_shared//2
        tot_likes += like
        people_shared = like*3
        n -= 1
    return tot_likes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
