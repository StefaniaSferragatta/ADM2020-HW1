
A=set(map(int, ((input().split())))) #set A
n = int(input()) #n is the number of the other set
if len(A) in range (1,501):
    if n in range (1,21):
        for _ in range (n):
            s = set(input().split())
            if len(s) in range (1,101):
                if not A.issuperset(s):
                    print(False)
                    exit()
                else:
                    print(True)