n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

def remove_block(start, end):
    temp = []
    for i in range(len(arr)):
        if start-1 <= i < end:
            pass
        else:
            temp.append(arr[i])
    return temp

# 첫번째
s, e = map(int, input().split())
arr = remove_block(s, e)
# 두번째
s, e = map(int, input().split())
arr = remove_block(s, e)

# 결과
print(len(arr))
if len(arr) > 0:
    for item in arr:
        print(item)