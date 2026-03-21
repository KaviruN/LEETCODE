nums = [5, 2, 3]

# def a(nums):
#     prefixes = [1]
#     suffixes = [1]#5 , 
#     answer = []
#     for i in range(len(nums) - 1):
#         prefixes.append(nums[i] * prefixes[i])
#     for j in range(len(nums) - 1, 0, -1):
#         suffixes.append(nums[j] * suffixes[len(suffixes) - 1])
#         # print(j)
#     suffixes = list(reversed(suffixes))
#     for k in range(len(nums)):
#         answer.append(prefixes[k] * suffixes[k])
#     return answer
#     # return prefixes, list(reversed(suffixes))


def a(nums):
    prefixes = 1
    answer = [1]  * len(nums) # just to add a fix len to the list
    suffixes = 1#5 , 
    for i in range(len(nums)):
        answer[i] = (nums[i] * prefixes[i])
    # for j in range(len(nums) - 1, 0, -1):
    return prefixes




print(a(nums))
# a(nums)