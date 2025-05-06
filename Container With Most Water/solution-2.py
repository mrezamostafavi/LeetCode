height = [1,8,6,2,5,4,8,3,7]

max = 0
i = 0
j = 1

while True:
    area = min(height[i], height[j])*(j-i)
    if area > max:
        max = area
    if j == len(height)-1:
        if i == len(height)-2:
            break
        i += 1
        j = i + 1
    else:
        j += 1
    
print(max)
        


