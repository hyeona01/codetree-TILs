n, t = map(int,input().split())
belt = list(map(int, input().split()))
belt += list(map(int, input().split()))

temp = belt[-1]
for i in range(n*2-2, -1, -1):
    belt[i+1] = belt[i]
belt[0] = temp

for i in range(2):
    for j in range(n):
        print(belt[n*i+j], end=' ')
    print()