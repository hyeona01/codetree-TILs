def lcm(n, m):
    return int((n * m) / gcd(n, m))

def gcd(n, m):
    r = 0
    while n%m != 0:
        r = n % m
        n = m
        m = r
    return m

n,m = map(int, input().split())

print(lcm(n,m))