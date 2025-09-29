nums = [3,4,5,6]

target = 7

def towSum(nums, target):
    numhash = {} #val:index {3: 0, 4: 1, 5: 2, 6: 3}
    for i, n in enumerate(nums):
        numhash[n] = i


towSum(nums, target)