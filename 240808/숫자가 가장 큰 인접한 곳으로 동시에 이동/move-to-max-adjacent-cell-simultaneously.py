# 상하좌우
dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]

# 입력받기
n, m, t = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
start = []
for i in range(m):
    start.append(list(map(int, input().split())))

# count, next_count 배열 생성
count = [[0 for _ in range(n)] for _ in range(n)]
next_count = [[0 for _ in range(n)] for _ in range(n)]

# 격자를 벗어나는지 확인하는 함수
def in_range(r, c):
    return r<n and r>=0 and c<n and c>=0
# 구슬이 움직이는 함수
def move(r, c):
    # 가장 커야하고, 동일하다면 상하좌우 우선순위 적용
    max_num = 0
    is_changed = False
    for dx, dy in zip(dxs, dys):
        if in_range(r+dx, c+dy) and max(arr[r][c], max_num) < arr[r+dx][c+dy]:
            max_num = arr[r+dx][c+dy]
            next_count[r+dx][c+dy] += 1
            is_changed = True
    if not is_changed:
        next_count[r][c] += 1

# 초기 위치를 count 격자에 표시하기
for s in start:
    i = s[0]-1
    j = s[1]-1
    count[i][j] = 1

# time 만큼 반복하기
for time in range(t):
    # next_count 초기화
    next_count = [[0 for _ in range(n)] for _ in range(n)]
    # 격자에 구슬이 있으면 다음 위치로 이동시키기
    for i in range(n):
        for j in range(n):
            if count[i][j]:
                move(i, j)
    count = next_count

    # count 격자에 2이상이 있는지 확인하고 0으로 바꾸기
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0

result = 0
for i in range(n):
    for j in range(n):
        result += count[i][j]
print(result)