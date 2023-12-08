graph = {}

def check_finish(nodes):
    for node in nodes:
        if node[-1] != 'Z':
            return False
    return True

with open('day8.txt', 'r') as file:
    moves = file.readline().strip()
    #print(moves)
    line = file.readline()
    #print(line)
    line = file.readline()
    #print(line)
    while line:
        graph[line[:3]] = [line[7:10], line[12:15]]
        line = file.readline()
    curr = []
    for key in graph.keys():
        if key[-1] == 'A':
            curr.append(key)

    curr = [curr[5]]
    counter = 0
    while not check_finish(curr):
        for move in moves:
            if check_finish(curr):
                break
            new = []
            for node in curr:
                if move == 'L':
                    new.append(graph[node][0])
                else:
                    new.append(graph[node][1])
            counter += 1
            curr = new
    print(counter)

multiples = [12169, 20093, 20659, 22357, 13301, 18961]
