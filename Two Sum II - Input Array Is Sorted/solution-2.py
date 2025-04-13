numbers = [2,7,11,15]
target = 9

idx = [0, 0]

for i in range(len(numbers)-1):
    idx[0] = i + 1
    nums = numbers[:i]+numbers[i+1:]
    if target - numbers[i] in numbers:
        idx[1] = nums.index(target - numbers[i]) + 2
        print(idx)
        break
