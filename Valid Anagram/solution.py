s = "aacc"
t = "ccac"

if set(s) == set(t) and len(s) == len(t):
    for i in t:
        if s.count(i) == t.count(i):
            continue
        else:
            print("False")
            break
    print("True")
else:
    print("False")