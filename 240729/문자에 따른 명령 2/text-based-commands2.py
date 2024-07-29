x, y = 0, 0
# 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir = input()
dir_num = 0
for i in dir:
    if i == 'L':
        dir_num -= 1
    elif i == 'R':
        dir_num += 1
    else:
        x += dx[dir_num%4]
        y += dy[dir_num%4]

print(x, y)