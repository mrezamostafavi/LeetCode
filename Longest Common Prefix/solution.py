strs = ["ab", "a"]
strs = sorted(strs)
c = ""
o = 0
ref = strs[0]
for j in range(len(ref)):
    z = 0
    for i in range(1, len(strs)):
        if ref[j] in strs[i][j]:
            z += 1
        else:
            o = 1
            break
    if z == len(strs) - 1:
        c = c + ref[j]
    if o == 1:
        break
print(c)