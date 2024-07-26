n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def solution(a, b):
    if b[0] in a:
        idx = a.index(b[0])
        if a[idx:(idx+len(b))] == b:
            return True
        else: return False

if solution(A,B):
    print("Yes")
else:
    print("No")