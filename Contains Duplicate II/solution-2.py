nums = [1,0,1,1]
k = 1

c = {}

for i in range(len(nums)):
    if nums[i] in c:
        if abs(c[nums[i]] - i) <= k:
            print('True')
            break
        else:
            c[nums[i]] = i
    else:
        c[nums[i]] = i
else:
    print("Fasle")