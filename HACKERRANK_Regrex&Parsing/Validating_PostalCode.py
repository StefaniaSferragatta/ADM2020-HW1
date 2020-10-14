#Error at 3/7 test cases

regex_integer_in_range = r"<[1-9][\d]{5}"	# P must be a number in the range from 100000 to 900000 inclusive.
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"#r"(\d)(?=\d\1)"	# P must not contain more than one alternating repetitive digit pair.

import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)