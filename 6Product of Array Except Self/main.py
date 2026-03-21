nums = [5, 2, 3]

def a(nums):
    prefixes = [1]
    suffixes = [1]
    answer = []
    for i in range(len(nums) - 1):
        prefixes.append(nums[i] * prefixes[i])
    # for j in range(len(nums) - 1, 0, -1):
    #     suffixes.append(nums[j] * nums[j - 1])
    # # for k in range(nums):
    # #     answer.append(prefixes[k] * suffixes[k])
    # # return answer
    return prefixes #,suffixes



print(a(nums))
# a(nums)