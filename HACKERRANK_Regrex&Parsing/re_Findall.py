# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"
string = input()
print(*re.findall("(?=[%s]([%s]{2,})[%s])"%(consonants,vowels,consonants),string, re.IGNORECASE) or [-1], sep="\n")
