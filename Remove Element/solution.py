nums = [3,2,2,3]
val = 3
z = 0
x = len(nums)
while val in nums:
    nums.remove(val)
    z += 1

print(x-z)
