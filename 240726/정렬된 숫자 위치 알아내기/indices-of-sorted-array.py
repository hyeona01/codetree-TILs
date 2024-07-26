N = int(input())
arr = list(map(int,input().split()))
num_list = [[i, arr[i]] for i in range(N)]

sorted_lst = sorted(num_list, key= lambda num : num[1])
for i in range(N):
    print(sorted_lst.index(num_list[i])+1, end=" ")

# print(num_list)
# print(sorted_lst)