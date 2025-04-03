t = "',.pyfgcrl/=aoeuidhtns-\\;qjkxbmwvz"
s = "qwertyuiop[]asdfghjkl;'\\zxcvbnm,./"

c = s
z = t
if len(s) != len(t) or len(set(s)) != len(set(t)):
    print('False')
else:
    while s:
        c = c.replace(s[0], t[0].upper())
        # print(c.lower())
        s = s.replace(s[0],"")
        t = t.replace(t[0],"")
    print(c.lower())
    print(z)
    if c.lower() == z:
        print("True")
    else:
        print("False")