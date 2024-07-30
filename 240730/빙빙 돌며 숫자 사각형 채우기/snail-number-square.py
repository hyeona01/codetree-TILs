# 우 하 좌 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
lst_2d = [[0 for _ in range(m)] for _ in range(n)]

def is_range(r, c):
    return r>-1 and r<n and c>-1 and c<m

dir = 0
r, c = 0, 0
for num in range(1, (n * m)+1):
    lst_2d[r][c] = num
    num += 1

    r, c = r+dy[dir], c+dx[dir]
    if is_range(r, c) and lst_2d[r][c] == 0:
        pass
    else:
        r, c = r-dy[dir], c-dx[dir]
        dir = (dir + 1) % 4
        r, c = r+dy[dir], c+dx[dir]

for row in lst_2d:
    for col in row:
        print(col, end=' ')
    print()