cube = lambda x: pow(x,3) # complete the lambda function

def fibonacci(n):
    l=[]
    for i in range(0 ,n):
        if(i==0):
            l.append(0)
        elif(i==1):
            l.append(1)
        elif(i>1):
            sum_ =l[i-1]+l[i-2]
            l.append(sum_)
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))