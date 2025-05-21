nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

c = []

for i in nums1:
    for j in nums2:
        c.append((i, j))
c.sort(key=lambda x: x[0] + x[1])

print(c[:k])