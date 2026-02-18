n =int(input()) 
s = input()
count_Anton = 0
count_Danik = 0
for character in s:
     if character == "A":
	     count_Anton += 1
     elif character == "D":
	        count_Danik += 1
if count_Anton > count_Danik:
	print("Anton")
elif count_Danik > count_Anton:
	print("Danik")
else:
	print("Friendship")
	
