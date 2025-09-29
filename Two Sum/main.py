nums = [3,2,4]

target = 6

def towSum(nums, target):
    numhash = {} #val:index {3: 0, 4: 1, 5: 2, 6: 3}
    for i, n in enumerate(nums):
        diff = target - n
        numhash[n] = i
        if diff in numhash and n != diff: #and you may not use the same element twice.
            return [numhash[diff], i]




print(towSum(nums, target))

# a = {3: 0, 4: 1, 5: 2, 6: 3}

# if 3 in a:
#     print(f'3:{a[3]}')