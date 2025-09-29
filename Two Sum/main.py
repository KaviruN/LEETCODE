nums = [3,4,5,6]

target = 7

def towSum(nums, target):
    numhash = {} #val:index
    for i in nums:
         numhash[nums[i]] = i
    print(numhash)


