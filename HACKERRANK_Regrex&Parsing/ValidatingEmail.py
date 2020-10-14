
import re

n = int(input())
for _ in range(n):
    name, email = map(str, input().split())
    check_email = re.search(r"(?:\b)([^\s]*\@[^\s]*\.[a-zA-Z]{2,4})(?:\b)", email)
    if check_email:
        print(name + ' <' + check_email.group(1) + '>')

