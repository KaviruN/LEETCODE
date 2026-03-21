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
    answer = [1]  * len(nums) # just to add a fix len to the list

    prefixes = 1
    for i in range(len(nums)):
        answer[i] = prefixes
        prefixes *= nums[i]

    postfix = 1
    for j in range(len(nums) - 1, -1, -1):
        answer[j] *= postfix
        postfix *= nums[j]
    return answer




print(a(nums))
# a(nums)