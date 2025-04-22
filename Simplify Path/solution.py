path = "/a/./b/../../c/"

c = []
z = 0
path = path.split("/")[::-1]

for i in path:
    if i in ("", "."):
        continue
    if i == "..":
        z += 1
        continue
    elif z >> 0:
        z -= 1
        continue
    else:
        c.append(i)
c = "/" + "/".join(c[::-1])
print(c)