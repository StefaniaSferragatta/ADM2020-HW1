#UNION
n_english = int(input())
english_student = input().split()
n_french = int (input())
french_student = input().split()

set_english = set(english_student)
set_french = set(french_student)
one_sub = set_english.union(set_french)
output = len(one_sub)
print (output)