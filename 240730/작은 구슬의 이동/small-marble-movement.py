# 상 우 좌 하
dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]

mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3,
}

def is_current(x, y):
    return x<n and x>-1 and y<n and y>-1

n, t = map(int, input().split())
r, c, d = input().split()
r = int(r) - 1
c = int(c) - 1

dir = mapper[d]
for _ in range(t):
    c += dx[dir]
    r += dy[dir]
    if is_current(r, c):
        pass
    else:
        c -= dx[dir]
        r -= dy[dir]
        dir = 3 - dir

print(r+1, c+1)