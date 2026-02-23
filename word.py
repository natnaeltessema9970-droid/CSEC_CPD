s = input()
count_upper = 0
count_lower = 0
for character in s:
	if character.isupper():
		count_upper += 1
	elif character.islower():
		count_lower += 1
if count_upper > count_lower:
	print(s.upper())
elif count_lower > count_upper:
	print(s.lower())
elif count_lower == count_upper:
	print(s.lower())