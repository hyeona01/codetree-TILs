n, m = map(int, input().split())

arr_2d =[[0 for i in range(m)] for j in range(n)]
num = 0

for i in range(m):
    if i%2 == 0:
        for j in range(n):
            arr_2d[j][i] = num
            num += 1
    else:
        for j in range(n):
            arr_2d[n-1-j][i] = num
            num += 1

for i in range(n):
    for j in range(m):
        print(arr_2d[i][j], end=" ")
    print()