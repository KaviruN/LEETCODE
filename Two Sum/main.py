nums = [3,4,5,6]

target = 7

def towSum(nums, target):
    numhash = {} #val:index
    for i, n in enumerate(nums):
        numhash[n] = i
    print(numhash)


towSum(nums, target)