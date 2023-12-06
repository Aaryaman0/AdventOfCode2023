from collections import defaultdict

with open('day4.txt', 'r') as file:
    arr = []
    final = 0
    cards = defaultdict(int)
    current = 1
    for line in file:
        cards[current] += 1
        h = {}
        nums = line[9:].split(' ')
        switch = False
        counter = 0
        for num in nums:
            if num == '':
                continue
            if switch:
                if int(num) in h:
                    counter += 1
                    #print(num)
            elif num == '|':
                switch = True
            else:
                h[int(num)] = True
        #print(current, counter)
        for idx in range(1, counter+1):
            cards[current + idx] += cards[current]
        #print(cards)
        current += 1
    for idx in cards.keys():
        #print(cards[idx])
        final += cards[idx]
    
    print(final)



