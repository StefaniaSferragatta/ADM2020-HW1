N,M = map(int, input().split())
max = 1001
items = []
if N in range (1,max):
    if M in range (1,max):
        for _ in range(N):
            items.append(list(map(int, input().split())))
        K = int(input())
        if K in range (0,M+1):
            sorted_items = sorted (items, key = lambda record: record[K])
            #"record" is the argument of the lambda function that returns the value of "record" at key "K".
            #I'm using this to grab the values from the dictionary with a given key, "K".
            for i in sorted_items:
                print (*i)
