nums = [12,28,83,4,25,26,25,2,25,25,25,12]
target = 213

nums = sorted(nums)[::-1]
j = 1
i = 0
step = 1

while True:

    if sum(nums[i:j]) >= target:
        print(step)
        break
    j += 1
    i += 1
    if j > len(nums):
        i = 0
        step += 1
        j = step
        if step > len(nums):
            print(0)
            break



    
    