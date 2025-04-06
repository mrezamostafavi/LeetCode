nums = [0,0,1,1,1,2,2,3,3,4]

idx = []
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        idx.append(i)

for index in sorted(idx, reverse=True):
    del nums[index]

print(nums)