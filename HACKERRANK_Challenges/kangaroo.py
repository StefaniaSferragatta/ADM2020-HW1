#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    #velocity = distance / jump -> distance = velocity * jump
    #distance1 = x1+v1*jump
    #distance2 = x2+v2*jump
    #The distances are: jump(v1-v2) = x2-x1
    #so jump = x2-x1/(v1-v2)
    #if jump is int print YES, else NO

    start_position = abs(x2-x1)
    dist_jump = abs(v1-v2)
    calc = start_position % dist_jump
    if v1 < v2: #if the velocity of the first kangaroo is less than the velocity of the second, the first one will never reach the second kangaroo
        return "NO"
    if calc == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()
