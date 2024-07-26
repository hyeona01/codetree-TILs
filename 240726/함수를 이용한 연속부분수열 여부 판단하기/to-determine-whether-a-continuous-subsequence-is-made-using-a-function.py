n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def solution(a, b):
    if b[0] in a:
        idx = [i for i, value in enumerate(a) if value == b[0]]
        for i in idx:
            if a[i:(i+len(b))] == b:
                return True
    return False

if solution(A,B):
    print("Yes")
else:
    print("No")