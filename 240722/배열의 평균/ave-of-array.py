arr_2d = []
for _ in range(2):
    arr_2d.append(list(map(int, input().split())))

print(round(sum(arr_2d[0])/len(arr_2d[0]),1), round(sum(arr_2d[1])/len(arr_2d[1]),1))

all = 0
for c in range(4):
    cols_add = arr_2d[0][c]+arr_2d[1][c]
    print(round(cols_add/2,1), end=" ")
    all += cols_add
print()
print(round(all/8,1))