# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()
N = int(input()) #number of element
if N > 0 and N <= 100:
    for _ in range(N):
        command = input().split()
        if command[0] == "append":
            d.append(int(command[1]))
        elif command[0] == "pop":
            d.pop()
        elif command[0] == "popleft":
            d.popleft()
        elif command[0] == "appendleft":
            d.appendleft(int(command[1]))
    print(*d)
