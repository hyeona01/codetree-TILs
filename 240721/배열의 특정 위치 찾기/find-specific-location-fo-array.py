lst = list(map(int, input().split()))

sum_nums = lst[1::2]
average_nums = lst[2::3]

print(sum(sum_nums), round(sum(average_nums)/len(average_nums),1))