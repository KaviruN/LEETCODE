nums = [1,2,3,4]

def a(nums):
    pre = [1]
    suf = []
    for i in range(len(nums) + 1):
        pre.append(nums[i + 1] * nums[i])
    return pre


print(a(nums))