arr_2d = []
for i in range(5):
    arr_2d.append(list(input().split()))
    for j in range(3):
        arr_2d[i][j] = arr_2d[i][j].upper()
        print(arr_2d[i][j], end=" ")
    print()