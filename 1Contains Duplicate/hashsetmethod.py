nums = [1, 2, 3, 3]

def a(nums):
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

print(a(nums))