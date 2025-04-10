s = "   fly me   to   the moon  "
s = s.split(" ")[::-1]
for i in s:
    if len(i) > 0:
        print(len(i))
        break
