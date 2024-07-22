n, m = map(int, input().split())

arr1 = []
for _ in range(n):
    arr1.append(list(map(int, input().split())))
arr2 = []
for _ in range(n):
    arr2.append(list(map(int, input().split())))

for r in range(n):
    for c in range(m):
        if arr1[r][c] == arr2[r][c]:
            print(0, end=" ")
        else: print(1, end=" ")
    print()