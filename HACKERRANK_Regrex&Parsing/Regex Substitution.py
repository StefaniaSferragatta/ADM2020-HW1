import re

N = int(input())
for _ in range(N):
    string = ''
    text = input()
    string = re.sub(r'(?<= )&&(?= )','and',text)
    string = re.sub(r'(?<= )\|\|(?= )','or',string)
    print (string)