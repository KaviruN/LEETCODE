nums = [1,2,3,1]

nums = sorted(nums)

print(nums)

for i in range(len(nums) + 1):
    if nums[i] in nums[i + 1]:
        return True
    else:
        return False