nums = [1, 2, 3, 0, 2]

def a(nums):
    numset = set()
    for i in nums:
        if i in numset:
            return True
        numset.add(i)
    return False



print(a(nums))