from decimal import Decimal
n = int(input()) #number of students' record
student_marks = {}
if n>= 2 and n<=10:
    #if len(student_marks) == 3:
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name] #Extract into a list the mark values of the student to query
    total_scores = sum(query_scores) #Do the sum of the query student's scores in the list
    avg = Decimal(total_scores / 3) #Convert the floats to decimals and average the scores
    mean = round(avg, 2) #save the mean of the averaged scores and correct to two decimals
    print(mean) #print the mean
