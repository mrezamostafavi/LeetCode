prices = [7,6,4,3,1]

c = []

for i in range(len(prices)):
    for j in prices[i:]:
        if prices[i] == j:
            continue
        else:
            if prices[i] - j > 0:
                continue
            else:
                c.append(-1*(prices[i]-j))
if c:
    print(max(c))
else:
    print (0)

