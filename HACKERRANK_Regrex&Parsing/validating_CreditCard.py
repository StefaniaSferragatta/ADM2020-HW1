# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())
for i in range(N):
    credit_card_num = input()
    check1 = re.match(r"^(\d{4}-?){3}\d{4}$",credit_card_num)
    rep_credit_card = credit_card_num.replace("-", "")
    check2 = re.match(r"^([456])(?!\1{3})(?:(\d)(?!\2{3})){15}$",rep_credit_card)
    if check1 and check2:
        print("Valid")
    else:
        print("Invalid")