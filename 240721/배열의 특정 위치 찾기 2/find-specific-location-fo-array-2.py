nums = list(map(int,input().split()))

odd = sum(nums[0::2])
even = sum(nums[1::2])

print(abs(odd-even))