
import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    format_code = '%a %d %B %Y %H:%M:%S %z' #the format code, 'nameday numday month year hour:mins:sec timezone'
    t1 = datetime.strptime(t1,format_code) #create a datetime object from the given string (using the format code)
    t2 = datetime.strptime(t2,format_code)
    diff_sec = int((t1-t2).total_seconds()) #returns the difference of the dates t1 and t2 in seconds
    output = str(diff_sec) #convert it in string
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()
