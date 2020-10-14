# Enter your code here. Read input from STDIN. Print output to STDOUT
odd = []
even=[]
lower = []
upper = []
string = sorted (str(input()))

for i in string:
    if i.isalpha():
        if i.isupper():
            x = upper
        else:
            x = lower
    else:
        if int(i)%2 == 0:
            x = even
        else:
            x = odd
    x.append(i)

print("".join(lower+upper+odd+even))