def solution(a, b):
    if a>b:
        return b+10, a*2

a,b = map(int, input().split())

x, y = solution(a,b)
print(max(x,y), min(x,y))