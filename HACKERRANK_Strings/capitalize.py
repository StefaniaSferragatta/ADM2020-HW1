
import math
import os
import random
import re
import sys

def solve(s):
    capitalize = s.title() #returns a copy of the string in which first characters of all the words are capitalized.
    return capitalize

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
