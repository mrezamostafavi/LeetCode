intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

out = []
for i in intervals:
    if i[1] < newInterval[0]:
        out.append(i)
    elif i[0] > newInterval[1]:
        out.append(i)
    else:
        newInterval[0] = min(newInterval[0], i[0])
        newInterval[1] = max(newInterval[1], i[1])
out.append(newInterval)
out.sort(key=lambda x: x[0])
print(out)