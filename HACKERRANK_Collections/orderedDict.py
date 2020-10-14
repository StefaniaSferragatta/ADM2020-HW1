
from collections import OrderedDict

N = int(input())
d = OrderedDict()
if N > 0 and N < 100:
    for _ in range (N):
        name, space, s_price = input().rpartition(" ")
        price = int(s_price)
        if name in d.keys():
            d[name] = d[name] + price
        else:
            d[name] = price
    for key,value in d.items():
        print(key,value)