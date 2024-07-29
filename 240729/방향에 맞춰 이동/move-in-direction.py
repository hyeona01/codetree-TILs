N = int(input())
x, y = 0, 0

for i in range(N):
    d, n = input().split()
    if d == 'N':
        y += int(n)
    elif d == 'E':
        x += int(n)
    elif d == 'S':
        y -= int(n)
    elif d == 'W':
        x -= int(n)

print(x, y)