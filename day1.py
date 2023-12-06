
# PROBLEM 1

# with open('day1prob1.txt', 'r') as file:
#     counter = 0
#     for line in file:
#         first = 0
#         last = 0
#         n = len(line)
#         for idx in range(n):
#             if line[idx].isdigit():
#                 first = int(line[idx])
#                 break
#         for idx in range(n-1, -1, -1):
#             if line[idx].isdigit():
#                 last = int(line[idx])
#                 break
#         counter += first * 10 + last
#     print(counter)

# PROBLEM 2
with open('day1prob1.txt', 'r') as file:
    counter = 0
    h = {"one" : 1, "two" : 2, "three" : 3, "four": 4, "five": 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    for line in file:
        first = 0
        last = 0
        n = len(line)
        for idx in range(n):
            if line[idx].isdigit():
                first = int(line[idx])
                break
            if (n - idx) >= 6 and line[idx: idx+5] in h:
                first = h[line[idx: idx+5]]
                break
            if (n - idx) >= 5 and line[idx: idx+4] in h:
                first = h[line[idx: idx+4]]
                break
            if (n - idx) >= 4 and line[idx: idx+3] in h:
                first = h[line[idx: idx+3]]
                break
        for idx in range(n-1, -1, -1):
            if line[idx].isdigit():
                last = int(line[idx])
                break
            if (n - idx) >= 6 and line[idx: idx+5] in h:
                last = h[line[idx: idx+5]]
                break
            if (n - idx) >= 5 and line[idx: idx+4] in h:
                last = h[line[idx: idx+4]]
                break
            if (n - idx) >= 4 and line[idx: idx+3] in h:
                last = h[line[idx: idx+3]]
                break
        counter += first * 10 + last
    print(counter)
        