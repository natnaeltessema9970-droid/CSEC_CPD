x,y= map(int,input().split()) 
years = 0
while x<=y:
	x = x*3
	y = y*2
	years+=1
print(years)