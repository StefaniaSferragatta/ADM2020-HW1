output= []
N = int(input())
#print ("Write ", N," commands below:")
for i in range(N):
    cmd = input().split()
    for i in range(1, len(cmd)):
        cmd[i] = int(cmd[i])
    if cmd[0] == "insert" or cmd[0] == "INSERT":
        output.insert(cmd[1], cmd[2]) #cmd[1] is the index i, cmd[2] il the value
    elif cmd[0] == "print" or cmd[0] == "PRINT" :
        print (output)
    elif cmd[0] == "remove" or cmd[0] == "REMOVE":
        output.remove(cmd[1])
    elif cmd[0] == "append" or cmd[0] == "APPEND" :
        output.append(cmd[1])
    elif cmd[0] == "sort" or cmd[0] == "SORT":
        output.sort()
    elif cmd[0] == "pop" or cmd[0] == "POP":
        output.pop()
    elif cmd[0] == "reverse" or cmd[0] == "REVERSE":
        output.reverse()