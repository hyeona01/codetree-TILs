n = int(input())

result = [[0 for _ in range(n)] for _ in range(n)]

num = 1
for i in range(n):
    for j in range(n):
        result[j][i] = num
        num += 1

for r in range(n):
    for c in range(n):
        print(result[r][c], end=" ")
    print()