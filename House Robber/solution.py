nums = [2,7,9,3,1]

pre = 0
cur = 0
for i in nums:
    pre, cur = cur, max(cur, pre+i)
print(cur)
