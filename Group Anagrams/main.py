strs = ["act","pots","tops","cat","stop","hat"]

def groupAnagrams(strs):
    strsCount = {}

    for i in range(len(strs)):
        for char in range(len(strs)):
            strsCount[strs[i]] = [strs[i]]
    print(strsCount)


groupAnagrams(strs)