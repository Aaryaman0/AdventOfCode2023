# from collections import defaultdict

# with open('day5.txt', 'r') as file:
#     line = file.readline()
#     arr = list(map(int, line[7:].split(' ')))
#     line = file.readline()
#     line = file.readline()
#     line = file.readline()
#     h = {}
#     while line:
#         if line == "\n":
#             line = file.readline()
#             continue
#         if not line[0].isdigit():
#             copy = []
#             for num in arr:
#                 change = False
#                 for key, value in h.items():
#                     if num >= key and num <= key + value[1]:
#                         diff = num - key
#                         copy.append(diff + value[0])
#                         change = True
#                         break
#                 if not change:
#                     copy.append(num)
#             arr = copy 
#             h = {}
#             print(arr)
#         else:
#             new = list(map(int, line.split(' ')))
#             h[new[1]] = [new[0], new[2]]
#         line = file.readline()
#     copy = []
#     for num in arr:
#         change = False
#         for key, value in h.items():
#             if num >= key and num <= key + value[1]:
#                 diff = num - key
#                 copy.append(diff + value[0])
#                 change = True
#                 break
#         if not change:
#             copy.append(num)
#     print(min(copy))


with open('day5.txt', 'r') as file:
    line = file.readline()
    old = list(map(int, line[7:].split(' ')))
    arr = []
    for idx in range(0, len(old), 2):
        arr.append([old[idx], old[idx] + old[idx+1] - 1])
    line = file.readline()
    line = file.readline()
    line = file.readline()
    h = {}
    while line:
        if line == "\n":
            line = file.readline()
            continue
        if not line[0].isdigit():
            copy = []
            print(arr)
            print(h)
            i = 0
            while i < len(arr):
                pair = arr[i]
                change = False
                for key, value in h.items():
                    print(key, value, pair)
                    if pair[0] >= key and pair[1] <= key + value[1]:
                        diff = pair[0] - key
                        diff2 = pair[1] - (key + value[1])
                        copy.append([value[0] + diff, value[0] + value[1] + diff2])
                        change = True
                        print("A")
                        break
                    elif pair[0] >= key and pair[0] <= key + value[1]:
                        diff = pair[0] - key
                        copy.append([diff + value[0], value[0] + value[1]])
                        pair[0] = key + value[1]
                        print("B")
                    elif pair[1] <= key + value[1] and pair[1] >= key:
                        diff2 = pair[1] - (key + value[1])
                        copy.append([value[0], value[0] + value[1] + diff2])
                        pair[1] = key
                        print("C")
                    elif pair[1] >= key + value[1] and pair[0] <= key:
                        copy.append([value[0], value[0] + value[1]])
                        pair[1] = key
                        arr.append([key + value[1], pair[1]])
                if not change:
                    copy.append(pair)
                i += 1
            arr = copy 
            h = {}
        else:
            new = list(map(int, line.split(' ')))
            h[new[1]] = [new[0], new[2]]
        line = file.readline()
    copy = []
    i = 0
    while i < len(arr):
        pair = arr[i]
        change = False
        for key, value in h.items():
            print(key, value, pair)
            if pair[0] >= key and pair[1] <= key + value[1]:
                diff = pair[0] - key
                diff2 = pair[1] - (key + value[1])
                copy.append([value[0] + diff, value[0] + value[1] + diff2])
                change = True
                print("A")
                break
            elif pair[0] >= key and pair[0] <= key + value[1]:
                diff = pair[0] - key
                copy.append([diff + value[0], value[0] + value[1]])
                pair[0] = key + value[1]
                print("B")
            elif pair[1] <= key + value[1] and pair[1] >= key:
                diff2 = pair[1] - (key + value[1])
                copy.append([value[0], value[0] + value[1] + diff2])
                pair[1] = key
                print("C")
            elif pair[1] >= key + value[1] and pair[0] <= key:
                copy.append([value[0], value[0] + value[1]])
                pair[1] = key
                arr.append([key + value[1], pair[1]])
        if not change:
            copy.append(pair)
        i += 1
    print(min(copy))
        
        