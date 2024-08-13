T = int(input())

dxs = [-1, 1, 0, 0]
dys = [0, 0, 1, -1]

# 구슬이 격자 안에 있는지 확인
def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

# 구슬을 1초 후로 이동시킴
def move(x, y):
    nx = x + dxs[d]
    ny = y + dys[d]

    return nx, ny

# x, y 값에 맞는 인덱스 찾기
def find_idx():
    return bead['x'] == x and bead['y'] == y
# 구슬이 충돌했는지 확인(충돌한 구슬 삭제)
def bump(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 1:
                filtered_list = list(filter(find_idx, bead))#격자에 있는 구슬 확인
                for lst in filtered_list:
                    bead.remove(lst)#겹치는 구슬들을 bead 배열에서 삭제

# 이제 시작해볼까..
for time in range(T):
    n, m = map(int, input().split())

    bead = [] #구슬 담기
    arr = [[0 for _ in range(n)] for _ in range(n)] #n*n격자
    temp = [[0 for _ in range(n)] for _ in range(n)]

    # 1차원 배열에 구슬 초기정보 담기
    for _ in range(m):
        x, y, d = input().split()
        if d == 'U':
            d = 0
        elif d == 'D':
            d = 1
        elif d == 'R':
            d = 2
        elif d == 'L':
            d = 3
        bead.append({
            'x' : int(x)-1,
            'y' : int(y)-1,
            'd' : d
        })
        arr[int(x)-1][int(y)-1] = 1 #격자 위 구슬 초기값 설정

    # 움직여보기..
    for i in range(m):
        now_bead = bead[i]
        print(now_bead, "응애")
        nx = now_bead['x'] + dxs[now_bead['d']]
        ny = now_bead['y'] + dys[now_bead['d']]
        if in_range(nx, ny):
            temp[nx][ny] += 1
        else:
            # 방향 바꿔주기ㅠ
            if now_bead['d'] == 0 : now_bead['d'] = 1
            elif now_bead['d'] == 1 : now_bead['d'] = 0
            elif now_bead['d'] == 2 : now_bead['d'] = 3
            elif now_bead['d'] == 3 : now_bead['d'] = 2
    
    # 겹치는지 확인..
    for i in range(n):
        for j in range(n):
            arr[i][j] = temp[i][j]
    bump(arr)

    # 남은 구슬 출력
    print(len(bead))