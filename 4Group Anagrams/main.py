strs = ["act","cat","tan","nat","bat"]

def groupAnagrams(strs):
    hashmap = {}

    for i in range(len(strs)):
        s = ''.join(sorted(strs[i]))
        if s in hashmap:
            hashmap[s].append(strs[i])
        else:
            hashmap[s] = [strs[i]]

    return list(hashmap.values())
    
    

                
        
print(groupAnagrams(strs))






# a = {"abc":{'a':1}, "bcd":{'b':1...}}

# print(a["abc"]['a'])