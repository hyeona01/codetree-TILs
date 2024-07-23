n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

for row in range(n):
    arr[row][0] =1

for i in range(0, n):
    for j in range(1, i+1):
        if j==n-1:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j]+arr[i-1][j-1]

for ele in arr:
    for num in ele:
        if num != 0:
            print(num, end=" ")
    print()