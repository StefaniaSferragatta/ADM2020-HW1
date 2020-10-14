
import re

N = int(input())
if N>=1 and N <=10:
    for _ in range (N):
        number = input().strip()
        match_object = re.findall(r'^[7-9]\d{9}$',number)
        if len(match_object) != 0:
            print ("YES")
        else:
            print ("NO")