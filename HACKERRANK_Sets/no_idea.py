import math

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m= input().split() #n is the number of integers in the array arr, m is the number of elements in the disjoint set
arr = [int(x) for x in input().split()]
set1 = set([int(y) for y in input().split()])
set2 = set([int(z) for z in input().split()])
happiness = 0
max_ = pow(10,5)
if len(n)>= 0 and len(n)<=max_:
    if len(m) >= 0 and len(m)<=max_:
        #For each i integer in the array arr
        for i in arr:
        # if i is in set1, then add to happiness
            if i in set1:
                happiness +=1
            # Otherwise, your happiness does not change
            elif i in set2:
                happiness -=1
        print (happiness)