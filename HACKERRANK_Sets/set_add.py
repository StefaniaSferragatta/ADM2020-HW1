N = int(input())
distinct_country = set()
if N in range (0,1000):
    for i in range(N):
        distinct_country.add(input())
    output = len(distinct_country)
    print (output)