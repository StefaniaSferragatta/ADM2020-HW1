n = int(input()) #number of element of the set s
s = set(map(int, input().split())) #set s
N = int(input()) #number of comands
if n in range (0,21):
    if N in range (0,21):
        for _ in range(N):
            command = input().split()
            if command[0] == "pop":
                s.pop()
            elif command[0] == "remove":
                s.remove(int(command[1]))
            elif command[0] == "discard":
                s.discard(int(command[1]))
        output = sum (s)
        print(output)