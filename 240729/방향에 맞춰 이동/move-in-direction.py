N = int(input())
x, y = 0, 0

# W, S, N, E
dx, dy = [-1,0,0,1], [0,-1,1,0]

for i in range(N):
    d, n = input().split()
    dir = 0 # 방향

    n = int(n)
    if d == 'W':
        dir = 0
    elif d == 'S':
        dir = 1
    elif d == 'N':
        dir = 2
    elif d == 'E':
        dir = 3

    x, y = x+dx[dir]*n, y+dy[dir]*n

print(x, y)