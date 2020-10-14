# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n , m = map(int,input().split())
d = defaultdict(list)
if n >= 1 and n<= 10000:
    if m>= 1 and m <= 100:
        for i in range(1,n+1):
            d[input()].append(i)
        for i in range(m):
            character = input()
            if character not in d.keys():
                print(-1)
            else:
                print(*d[character])
