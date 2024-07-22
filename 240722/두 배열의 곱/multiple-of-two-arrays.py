arr1 = []
arr2 = []

for _ in range(3):
    arr1.append(list(map(int,input().split())))
input()
for _ in range(3):
    arr2.append(list(map(int,input().split())))

for r in range(3):
    for c in range(3):
        print(arr1[r][c]*arr2[r][c], end=" ")
    print()