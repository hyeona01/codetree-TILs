n, m = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]

num = 1
for i in range(m):
    r, c = map(int, input().split())
    arr[r-1][c-1] = num
    num += 1

for lst in arr:
    for num in lst:
        print(num, end=" ")
    print()