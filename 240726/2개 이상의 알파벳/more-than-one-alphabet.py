def solution(A):
    al = A[0]
    cnt = A.count(al)

    for i in range(cnt):
        A = A.replace(al, '')

    return A

A = input()
if solution(A) == '':
    print("No")
else:
    print("Yes")