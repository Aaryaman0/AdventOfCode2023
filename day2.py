# with open('day2.txt', 'r') as file:
#     counter = 0
#     line_num = 1
#     for line in file:
#         line = line[line.find(":") + 2:]
#         color_groups = line.split(';')
#         worked = True
#         h = {"red": 0, "blue": 0, "green": 0}
#         for group in color_groups:
#             # Split each group into individual color-count pairs
#             color_count_pairs = group.split(',')
#             # Iterate over each color-count pair
#             for pair in color_count_pairs:
#                 # Extract color and count
#                 parts = pair.strip().split()
#                 if len(parts) == 2:
#                     count, color = parts
#                     h[color] = min(h[color], int(count))
#             if not (h["red"] <= 12 and h["green"] <= 13 and h["blue"] <= 14):
#                 worked = False
#                 break
#         if worked:
#             counter += line_num
#             print(line_num)
#         line_num += 1
#     print(counter)

with open('day2.txt', 'r') as file:
    counter = 0
    for line in file:
        line = line[line.find(":") + 2:]
        color_groups = line.split(';')
        h = {"red": 0, "blue": 0, "green": 0}
        for group in color_groups:
            # Split each group into individual color-count pairs
            color_count_pairs = group.split(',')
            # Iterate over each color-count pair
            for pair in color_count_pairs:
                # Extract color and count
                parts = pair.strip().split()
                if len(parts) == 2:
                    count, color = parts
                    h[color] = max(h[color], int(count))
        sum = 1
        for key in h.keys():
            sum *= h[key]
        counter += sum
    print(counter)