arr = []

def allzero(nums):
    for num in nums:
        if num != 0:
            return False
    return True

def perforate(nums):
    counter = 0
    while not allzero(nums):
        new = []
        for i in range(1, len(nums)):
            new.append(nums[i] - nums[i-1])
        counter += new[-1]
        nums = new
    return counter

with open('day9.txt', 'r') as file:
    for line in file:
        arr.append(list(map(int, line.strip().split(' '))))
    # print(arr)
    counter = 0
    for nums in arr:
        # counter += perforate(nums) + nums[-1]
        counter += perforate(nums[::-1]) + nums[0]
    print(counter)