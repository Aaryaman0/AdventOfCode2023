from collections import defaultdict

arr = []
totalrows = 0
rowlen = 0
counter = 0
h = defaultdict(list)

# def checkBounds(row, startcol, endcol, num):
#     # print(num)
#     global counter
#     print(arr[row][max(0, startcol-1): min(rowlen, endcol+2)])
#     for char in arr[row][max(0, startcol-1): min(rowlen, endcol+2)]:
#         if char != "." and not char.isdigit():
#             counter += num
#             return
#     if row - 1 >= 0:
#         print(arr[row-1][max(0, startcol-1): min(rowlen, endcol+2)])
#         for char in arr[row-1][max(0, startcol-1): min(rowlen, endcol+2)]:
#             if char != "." and not char.isdigit():
#                 counter += num
#                 return
#     if row + 1 < totalrows:
#         print(arr[row+1][max(0, startcol-1): min(rowlen, endcol+2)])
#         for char in arr[row+1][max(0, startcol-1): min(rowlen, endcol+2)]:
#             if char != "." and not char.isdigit():
#                 counter += num
#                 return

def checkBounds(row, startcol, endcol, num):
    # print(num)
    global h

    #print(arr[row][max(0, startcol-1): min(rowlen, endcol+2)])
    for idx in range(max(0, startcol-1), min(rowlen, endcol+2)):
        char = arr[row][idx]
        if char == "*":
            h[row * rowlen + idx].append(num)
            return
    if row - 1 >= 0:
        #print(arr[row-1][max(0, startcol-1): min(rowlen, endcol+2)])
        for idx in range(max(0, startcol-1), min(rowlen, endcol+2)):
            char = arr[row-1][idx]
            if char == "*":
                h[(row-1) * rowlen + idx].append(num)
                return
    if row + 1 < totalrows:
        #print(arr[row+1][max(0, startcol-1): min(rowlen, endcol+2)])
        for idx in range(max(0, startcol-1), min(rowlen, endcol+2)):
            char = arr[row+1][idx]
            if char == "*":
                h[(row+1) * rowlen + idx].append(num)
                return

with open('day3.txt', 'r') as file:
    for line in file:
        arr.append(line.strip())
    totalrows = len(arr)
    rowlen = len(arr[0])
    for line_num in range(totalrows):
        line = arr[line_num]
        start = 0
        end = 0
        s = ""
        idx = 0
        while idx < len(line):
            start = idx
            while idx < len(line) and line[idx].isdigit():
                s += line[idx]
                end = idx
                idx += 1
            if s != "":
                # print(s, line_num, start, end)
                checkBounds(line_num, start, end, int(s))
                s = ""
            idx += 1
    for key in h.keys():
        if len(h[key]) == 2:
            counter += (h[key][0] * h[key][1])
    print(counter)
