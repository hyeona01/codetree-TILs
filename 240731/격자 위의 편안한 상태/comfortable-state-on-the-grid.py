# 상 하 좌 우
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

def is_range(x, y):
    return x>-1 and x<n and y>-1 and y<n

n, m = map(int, input().split())
table = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    table[r][c] = 1

    cnt = 0
    for j in range(4):
        nc = c + dxs[j]
        nr = r + dys[j]
        if is_range(nc, nr) and table[nr][nc] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)