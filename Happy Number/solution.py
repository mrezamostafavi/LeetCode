n = 2

res = [n]
n = list(str(n))
z = 0

while z == 0:
    c = 0
    for i in n:
        c += int(i) ** 2
    if c == 1:
        print("True")
        break
    else:
        if c in res:
            print("False")
            break
        else:
            res.append(c)
            n = list(str(c))
