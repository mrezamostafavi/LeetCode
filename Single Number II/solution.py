nums = [0,1,0,1,0,1,99]

x = set(nums)
for i in x:
    if nums.count(i) < 3:
        print(i)
        break