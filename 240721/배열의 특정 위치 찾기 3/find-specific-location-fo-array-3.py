nums = list(map(int, input().split()))

idx = nums.index(0)

print(sum(nums[idx-3:idx]))