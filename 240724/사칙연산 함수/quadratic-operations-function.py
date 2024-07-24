import math

def solution(a,o,c):
    if o == '+':
        return int(a)+int(c)
    elif o == '-':
        return int(a)-int(c)
    elif o == '/':
        return int(a)/int(c)
    elif o == '*':
        return int(a)*int(c)

    
a, o, c = input().split()

print(a,o,c,"=",math.floor(solution(a,o,c)))