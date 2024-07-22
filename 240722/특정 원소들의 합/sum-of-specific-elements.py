arr_2d = []
for _ in range(4):
    arr_2d.append(list(map(int, input().split())))

result = 0
for r in range(0, 4):
    for c in range(r+1):
        result += arr_2d[r][c]

print(result)