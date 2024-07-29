# 상 하 좌 우
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

def is_valid(x, y):
    return x<n and x>-1 and y<n and y>-1

n = int(input())
# input_2d = [[0 for in range(n)]for in range(n)]
input_2d = []
for _ in range(n):
    input_2d.append(list(map(int, input().split())))

result = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dir in range(4): # 상하좌우 확인
            nx = j + dxs[dir]
            ny = i + dys[dir]
            if is_valid(nx, ny) and input_2d[ny][nx] == 1:
                cnt += 1
        if cnt >= 3:
            result += 1

print(result)