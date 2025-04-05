nums = [4,1,2,1,2]

z = 0
nums = sorted(nums)
for i in range(0,len(nums)-1,2):

    if nums[i] == nums[i+1]:
        pass
    else:
        print(nums[i])
        z = 1
if z == 0:
    print(nums[-1])

