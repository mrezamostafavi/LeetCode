numbers = [-1, 0]
target = -1

idx = [0, 0]

for i in range(len(numbers)-1):
    idx[0] = i + 1
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            idx[1] = j + 1
            print(idx)
            break

