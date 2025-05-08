s = "dvdf"

max = 0
x = []

for i in s:
    if i in x:
        x = x[x.index(i)+1:]
        x.append(i)
    else:
        x.append(i)
        if len(x) > max:
            max = len(x)

print(max)