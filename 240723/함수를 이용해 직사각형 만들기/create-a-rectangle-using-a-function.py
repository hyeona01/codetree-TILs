def square(n,m):
    arr = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end="")
        print()
    return arr

n, m = map(int, input().split())

square(n,m)