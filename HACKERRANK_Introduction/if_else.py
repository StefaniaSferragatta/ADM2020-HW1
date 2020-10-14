import math
import os
import random
import re
import sys
#1/8 test cases failed

if __name__ == '__main__':
    n = int(input().strip())
    if n < 1 or n > 100:
        print ("Not valid input number, retry.")
    else:
        r1 = range (2, 5)
        r2 = range (6,20)
        if (n % 2)==0 and n in r1: #if n is even and is in range (2,5)
            print ("Not Weird")
        elif (n % 2)==0 and n in r2: #if n is even and is in range (6,20)
            print ("Weird")
        elif (n % 2)==0 and n > 20: #if n is even and is greater than 20
            print ("Not Weird")
        elif (n % 2)!=0: #if n is odd
            print ("Weird")
