nums = [1,1,1,2,2,3]
k = 2

def topKelements(nums, k):
    hashmap = {}#1:3,2:2,3:1
    freq = [[] for i in range(len(nums) + 1)] #[[], [], [], [], [], [], []] -> [[], [3], [2], [1], [], [], []] 
    for n in nums:
        hashmap[n] = hashmap.get(n, 0) + 1
    for n, c in hashmap.items():
        freq[c].append(n)

    res = []

    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res

print(topKelements(nums, k))