x = 4

i = 1
a = 0
while a <= x:
    a = i * i
    if a == x:
        print(i)
        break
    if a > x:
        print(i-1)
        break
    i += 1
