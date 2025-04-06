nums = [2,2,1,1,1,2,2]

x = list(set(nums))

for i in x:
    y = nums.count(i)
    if y > (len(nums)/2):
        print(i)