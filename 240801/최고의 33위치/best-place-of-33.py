n = int(input())

coin_table = []
for _ in range(n):
    coin_table.append(list(map(int, input().split())))

result = 0

for i in range(n-3+1):
    for j in range(n-3+1):
        cnt = 0
        for z in range(3):
            cnt += coin_table[i][j+z] + coin_table[i+1][j+z] + coin_table[i+2][j+z]
        result = max(result, cnt)

print(result)