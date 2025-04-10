nums = [1,2,3,1,2,3]
k = 2
c = []
z=0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if i == j:
            continue
        else:
            if nums[i] == nums[j]:
                if abs(i - j) <= k:
                    print("True")
                    z = 1
                else:
                    continue

if z == 0:
    print("False")