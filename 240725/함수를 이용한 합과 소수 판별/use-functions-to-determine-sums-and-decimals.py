def is_prime(n):
    if n == 1: False
    for i in range(2, 9):
        if n%i == 0 :
            return False
    return True

def is_even(n):
    num = str(n)
    sum = 0
    for i in num:
        sum += int(i)
    if sum % 2 == 0:
        return True
    else: 
        return False

a, b = map(int, input().split())

result = 0
for i in range(a, b+1):
    if is_prime(i) and is_even(i):
        result += 1

print(result)