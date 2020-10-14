# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
s1=set(map(int, ((input().split()))))
input()
s2=set(map(int, ((input().split()))))
set1 = s1.difference(s2)
set2 = s2.difference(s1)
set3 = set1.union(set2)
output = sorted(set3)
for i in output:
    print(i)