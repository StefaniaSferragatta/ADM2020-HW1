import re

S = str(input())
if len(S)> 0 and len(S)<100:
    k = str(input())
p = re.compile(k)
m = p.search(S)
if m:
    while m:
        beginning = m.start()
        end = m.end() -1
        print((beginning,end))
        m = p.search(S, beginning+1)
else:
    print((-1, -1))
