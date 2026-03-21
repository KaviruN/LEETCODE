nums = [1,2,3,4]

def a(nums):
    pre = [1]
    suf = [1]
    for i in range(len(nums) - 1):
        pre.append(nums[i] * nums[i + 1])
    return pre


print(a(nums))