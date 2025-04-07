pattern = "papap"
s = "po io po io io"

s = s.split(' ')
pattern = list(pattern)
c = {}
z=0
if len(set(pattern)) != len(set(s)) or len(pattern) != len(s):
    print("False")
    z=1
else:
    for i in range(len(s)):
        if c.get(pattern[i]):
            if c[pattern[i]] == s[i]:
                continue
            else:
                print("False")
                z=1
        else:
            c[pattern[i]] = s[i]

if z != 1:
    print("True")