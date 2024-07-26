def solution(a, b):
    if a<b:
        return a+10, b*2
    else:
        return a*2, b+10

a,b = map(int, input().split())

x, y = solution(a,b)
print(x,y)