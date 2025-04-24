n = 5

c = 1
m = 0
while n > 0:
    c *= n
    n -= 1

while c % 10 == 0:
    m += 1
    c //= 10
print(m)