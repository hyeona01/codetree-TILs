def solution(n):
    if '3' in str(n) or '6' in str(n) or '9' in str(n) or n%3==0:
        return True
    
a, b = map(int, input().split())

result = 0
for i in range(a, b+1):
    if solution(i):
        result += 1

print(result)