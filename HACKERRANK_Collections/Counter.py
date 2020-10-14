from collections import Counter

max = pow(10,3)
X = int(input()) #number of shoes
shoe_size = list(map(int,input().split()))
count =Counter(shoe_size)
N = int(input()) #number of costumers
money=0
if X> 0 and X < max:
    if N>0 and N<=max:
        for i in range(0,N):
            size, price = list(map(int,input().split()))
            #if size> 2 and size < 20:
            #    if price > 20 and price <100:
            if size in count.keys():
                if count[size]!=0:
                    money += price
                    count[size] -= 1
        print(money)
