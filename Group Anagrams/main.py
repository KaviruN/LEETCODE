strs = ["act","cat"]

def groupAnagrams(strs):
    strsCount = {}

    for i in range(len(strs)):
        for char in range(len(strs[i])):
            if strs[i] not in strsCount:
                strsCount[strs[i]] = {}
            if strs[i][char] in strsCount[strs[i]]:
                strsCount[strs[i]][strs[i][char]] += 1
            else:
                strsCount[strs[i]][strs[i][char]] = 1

                
        
    print(strsCount)


groupAnagrams(strs)

# a = {"abc":{'a':1}, "bcd":{'b':1...}}

# print(a["abc"]['a'])