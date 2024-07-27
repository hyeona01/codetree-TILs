n, m = map(int, input().split())
A = list(map(int, input().split()))

for i in range(m):
    a1, a2 = map(int, input().split())
    print(sum(A[a1-1:a2-1+1]))