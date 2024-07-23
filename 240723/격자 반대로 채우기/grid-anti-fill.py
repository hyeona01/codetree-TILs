n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

num = 1

for i in range(n):
    if (n%2==0 and i%2==0) or (n%2==1 and i%2==1):
        for j in range(n):
            arr[n-1-j][n-1-i] = num
            num += 1
    else:
        for j in range(n):
            arr[j][n-1-i] = num
            num += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()