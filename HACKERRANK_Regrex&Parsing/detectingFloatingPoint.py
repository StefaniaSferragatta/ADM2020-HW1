import re

T = int(input())
for _ in range (T):
    N = input() #str(input())
    output = re.search(r"^[+-]?[0-9]*\.[0-9]+$", N)
    print (bool(output))
