prices = [7,1,5,3,6,4]

c = [0]
min = 10**4

for i in prices:
    if i < min:
        min = i
    else:
        c.append(i-min)

print(max(c))