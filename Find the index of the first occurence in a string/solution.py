haystack = "sadbutsad"
needle = "sad"

if needle in haystack:
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            print(i)
            break
else:
    print(-1)