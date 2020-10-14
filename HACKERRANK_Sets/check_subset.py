T =int(input()) #number of tests case
if T in range (0,21):
    for _ in range(T):
        num_a = input() #number of elements' A set
        A = set(input().split())
        num_b = input()
        B = set(input().split()) #number of elements' B set
        if len(A)>0 and len(A)<1001:
            if len(B) > 0 and len(B) < 1001:
                print(A.issubset(B))