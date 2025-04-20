strs = ["eat","tea","tan","ate","nat","bat"]

seen = {}
out = []

for word in strs:
    key = ''.join(sorted(word))
    if key in seen:
        out[seen[key]].append(word)
    else:
        seen[key] = len(out)
        out.append([word])
print(out)
    

            