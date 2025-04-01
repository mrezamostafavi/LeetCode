x = 121

z=0
if x <= 0:
    print("False")
else:
    x = list(str(x))
    if len(x) == 1:
        print("True")
    else:
        for i in range(int(len(x)/2)):
            if x[i] == x[-1-i]:
                continue
                
            else:
                print("False")
                z = 1
                break
        if z == 0:            
            print("True")
