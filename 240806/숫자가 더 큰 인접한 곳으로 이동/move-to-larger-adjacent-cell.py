n, sr, sc = map(int,input().split())
nx, ny = sr-1, sc-1

# 상 하 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
print(arr[nx][ny], end=' ')

def is_range(r, c):
    return r<n and r>=0 and c<n and c>=0

while is_range(nx, ny):
    max_num = arr[nx][ny]
    is_changed = False
    for dir in range(4):
        if is_range(nx+dxs[dir], ny+dys[dir]) and arr[nx+dxs[dir]][ny+dys[dir]] > max_num:
            max_num = arr[nx+dxs[dir]][ny+dys[dir]]
            nx, ny = nx+dxs[dir], ny+dys[dir]
            is_changed = True
            print(arr[nx][ny], end=' ')
            break
    if not is_changed:
        break