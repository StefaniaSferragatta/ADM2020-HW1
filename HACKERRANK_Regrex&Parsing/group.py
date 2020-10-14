import re

S = str(input())
if len(S)> 0 and len(S)< 100:
    m = re.search(r'([A-Za-z0-9])\1+', S)
    if m != None:
        output = m.group(1)
        print (output)
    else:
        output = "-1"
        print (output)
