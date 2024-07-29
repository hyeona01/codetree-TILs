x, y = 0, 0
# 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir = input()

nx, ny = 0, 0
for i in dir:
    if i == 'L':
        nx -= 1
        ny -= 1
    elif i == 'R':
        nx += 1
        ny += 1
    else:
        x += dx[nx%4]
        y += dy[ny%4]

print(x, y)