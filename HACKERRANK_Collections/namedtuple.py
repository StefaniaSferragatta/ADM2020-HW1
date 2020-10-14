import collections
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
Students = collections.namedtuple('Students', input())
marks = 0
for _ in range(N):
    values = input().split()
    students = Students(*values)
    marks += int(students.MARKS)
average =marks/N
print(average)