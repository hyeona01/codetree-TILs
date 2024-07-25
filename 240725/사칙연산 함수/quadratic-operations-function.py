def plus(a, b):
    return a+b

def minus(a, b):
    return a-b

def times(a, b):
    return a*b

def divide(a, b):
    return a//b

    
a, o, c = input().split()
a=int(a)
c=int(c)

if o == '+':
    print(a, o, c, "=", plus(a, c))
elif o == '-':
    print(a, o, c, "=", minus(a, c))
elif o == '*':
    print(a, o, c, "=", times(a, c))
elif o == '/':
    print(a, o, c, "=", divide(a, c))
else : False