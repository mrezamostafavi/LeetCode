nums = [1, 2, 3, 4]
peak = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        peak = i
    else:
        break
print(peak)