import re

T= int(input())
for _ in range (T):
    employee_UID = str(input())
    check = re.compile(r'(?!.*(.).*\1)(?=.*\d.*\d.*\d)(?=.*[A-Z].*[A-Z])[A-Za-z0-9]{10}').match(employee_UID)
    if not check:
        print('Invalid')
    else:
        print('Valid')