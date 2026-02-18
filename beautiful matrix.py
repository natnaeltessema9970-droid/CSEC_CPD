import math
matrix = []
for i in range(5):
	matrix.append(list(map(int,input().split())))
for i in range(5):
	for j in range(5):
		if matrix[i][j] == 1:
			row_index = i
			col_index = j
ans = abs(row_index-2) + abs(col_index-2)
print(ans)
