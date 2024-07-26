def solution(a, b):
    if a>b:
        return b+10, a*2
    else:
        return a+10, b*2

a,b = map(int, input().split())

result = solution(a,b)

for n in result:
    print(n, end=" ")