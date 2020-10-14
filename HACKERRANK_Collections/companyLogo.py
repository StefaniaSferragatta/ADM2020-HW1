import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = str(input())
    sort_s = sorted(s)
    frequence = Counter(sort_s) #passing a sorted string will keep all keys sorted in counter
    for char in frequence.most_common(3): #For the three most common characters along with their occurrence count.
        print(*char) #print the characters on a separate line.
