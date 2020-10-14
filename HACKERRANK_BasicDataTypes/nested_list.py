records = [] #create a nasted list for the students [[name0,mark0],[name1,mark1],...]
scorelist = [] #create a nasted list for the students' score
if __name__ == '__main__':
    n = int(input()) #number of students
    if n<= 5 and n >= 2: #check the constraint
        for _ in range (n): #for all the students
            name = input()  # students' name
            score = float(input())  # students' grade
            records += [[name,score]] #added at the nasted list the name and score of the student
            scorelist += [score] #added at the score list only the students' score
        sec_lowest = sorted(list(set(scorelist)))[1] #in order to sort them and find the second lowest grade

for name, grade in sorted(records): #then, it's sorted the nasted list too
    if grade == sec_lowest:
        print(name) #print all the students' names with second lowest grade