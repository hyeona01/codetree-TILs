n, m = map(int, input().split())
A = list(map(int, input().split()))

def solution(m):
    result = A[m-1]
    while m > 1:
        if m%2==1:
            m-=1
            result += A[m-1]
        else:
            m//=2
            result += A[m-1]
    return result

print(solution(m))