# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
if T >= 1 and T <= 5:
    for _ in range (T):
        n = int(input())
        if n >=1 and n <= pow(10,5):
            sideLengths = list(map(int,input().split()))
            count = 0
            if len(sideLengths) >=1 and len(sideLengths)<= pow(2,31):
                while (count < n-1 and sideLengths[count] >= sideLengths[count+1]):
                    count +=1
                while (count < n-1 and sideLengths[count] <= sideLengths[count+1]):
                    count +=1
                if count == len(sideLengths) - 1:
                    print ("Yes")
                else:
                    print ("No")