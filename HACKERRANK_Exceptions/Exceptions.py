T = int(input()) #T is the number of tests
if T in range (0,11):
    for _ in range (T):
        try:
            a, b = map(int,input().split())
            print (a//b)
        except ZeroDivisionError as e:
            print ("Error Code:",e)
        except ValueError as e:
            print ("Error Code:", e)


