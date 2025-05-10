nums = []

nums = sorted(set(nums))
if len(nums) == 0:
    print(0)
    exit()
max = 1
l = 1
pre = nums[0]
for i in range(1, len(nums)):
    if nums[i] - pre == 1:
        l += 1
    else:
        l = 1
    if l > max:
        max = l
    pre = nums[i]
print(max)