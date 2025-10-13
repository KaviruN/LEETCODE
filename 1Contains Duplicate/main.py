nums = [1, 2, 3, 2, 1]

nums = sorted(nums)

state = False


for i in range(len(nums) - 1):
    if not state and nums[i] == nums[(i + 1)]:
        state = True

        

print(state)