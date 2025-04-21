intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
c = []

intervals = sorted(intervals)
first = intervals[0][0]
last = intervals[0][1]
for i in intervals:
    if i[0] >= first and i[0] <= last:
        last = max(last, i[1])
    else:
        c.append([first, last])
        first = i[0]
        last = i[1]
c.append([first, last])
print(c)