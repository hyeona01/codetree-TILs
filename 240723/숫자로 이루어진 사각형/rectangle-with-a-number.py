def solution(N):
    arr = [[0 for _ in range(N)] for _ in range(N)]
    num = 1
    for i in range(N):
        for j in range(N):
            arr[i][j] = num
            if num < 9:
                num += 1
            else: num = 1

    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

solution(int(input()))