def is_prime(n):
    if n<2:
        return False
    for i in range(2, n-1):
        if n%i==0:
            return False
    return True

a,b = map(int, input().split())

result = 0
for i in range(a, b+1):
    if is_prime(i):
        result += i

print(result)