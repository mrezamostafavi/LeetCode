s = '[]'

o = '([{'
c = ')]}'
z = 0
open = 0
idx = []

if s[0] in c or s[-1] in o:
    print('False')
else:
    while open >= 0:
        for i in s:
            if i in o:
                idx.append(o.find(i)) 
                open += 1
            else:
                if open >> 0:
                    if idx[-1] == c.find(i):
                        idx.pop(-1)
                        open -= 1
                    else:
                        print('False')
                        z = 1
                        break
                else:
                    print('False')
                    z = 1
                    break
        if z == 1:
            break                
        if z != 1 and open == 0:
            print('True')
            break


