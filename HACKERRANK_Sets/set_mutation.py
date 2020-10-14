# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input()) #number of element of the set A
A = set(map(int, input().split())) #set A
N = int(input()) #number of other sets
if N in range (0,101):
    for _ in range (N):
        command = input().split()
        s = set(map(int, input().split()))  # set s
        option = command [0]
        if option== "update":
            A.update(s) # |=
        elif option == "intersection_update":
            A.intersection_update(s) # &=
        elif option == "difference_update":
            A.difference_update(s) # -=
        elif option == "symmetric_difference_update":
            A.symmetric_difference_update(s) #^=
    output = sum(A)
    print(output)

