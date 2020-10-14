#SIMMETRIC DIFFERENCE
n_english = int(input())
english_student = input().split()
n_french = int (input())
french_student = input().split()

set_english = set(english_student)
set_french = set(french_student)
sim_diff = set_english.symmetric_difference(set_french)
output = len(sim_diff)
print (output)
