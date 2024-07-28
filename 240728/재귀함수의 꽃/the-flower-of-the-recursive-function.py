def solution(N):
    if N == 0:
        return
    
    print(N, end=' ')
    solution(N-1)
    print(N, end=' ')

solution(int(input()))