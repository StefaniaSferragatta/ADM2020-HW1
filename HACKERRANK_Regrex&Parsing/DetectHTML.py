
import re

text = ''
cmt = r'<!.+-->' #comment
tag = r'<([^/][^>]*)>'
attr = r'([a-z]+)? *([a-z-]+)="([^"]+)'
n = int(input())

if n>0 and n<100:
    for _ in range(n):
        text = re.sub(cmt,r' ',(text+input()))

    for att in re.findall(tag, text):
        if ' ' in att:
            for att_val in re.findall(attr, att):
                if att_val[0]:
                    print(att_val[0])
                print('-> '+att_val[1]+' > '+att_val[2])
        else:
            print(att)
