n = int(input())
ls = list(map(int,input().rstrip().split()))
ls_sort = sorted(ls)
print(*ls_sort)