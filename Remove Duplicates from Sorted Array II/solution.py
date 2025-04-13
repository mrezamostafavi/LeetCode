nums = [0,0,1,1,1,1,2,3,3]

n = set(nums)
z = 0
for i in n:
    if nums.count(i) > 2:
        z += nums.count(i) - 2
        for j in range(nums.count(i) - 2):
            nums.remove(i)

print(nums)
print(len(nums))
    