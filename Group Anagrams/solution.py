strs = ["eat","tea","tan","ate","nat","bat"]

j = 0
c = []
out = []

for i in range(len(strs)):
    if strs[i] == "0" and len(strs) > 1:
        continue
    for j in range(i+1, len(strs)):
        if sorted(strs[i]) == sorted(strs[j]):
            c.append(strs[j])
            strs[j] = "0"

    out.append([strs[i]] + c)
    c = []
print(out)
            