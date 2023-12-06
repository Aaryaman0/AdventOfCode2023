with open('day6.txt', 'r') as file:
    dist = []
    time = []
    line = file.readline()
    time = list(map(int, line[6:].split(' ')))
    line = file.readline()
    dist = list(map(int, line[6:].split(' ')))
    print(time, dist)
    l = len(time)
    counter = 1
    for i in range(l):
        t = time[i]
        d = dist[i]
        start = 0
        end = 0
        for bt in range(t+1):
            if (t - bt) * bt > d:
                start = bt
                break
        for rbt in range(t, -1, -1):
            if (t - rbt) * rbt > d:
                end = rbt
                break
        print(end - start + 1)
        counter *= (end - start + 1)
    print(counter)


