s = "anagram"
t = "nagacam"

def isAnagram(s, t):
    sCount, tCount = {}, {}

    for i in range(len(s)):
        sCount[s[i]] = sCount.get(s[i], 0) + 1
        tCount[t[i]] = sCount.get(t[i], 0) + 1

    print(sCount, tCount)  


isAnagram(s, t)


# a = {}


# a['a'] = 1

# print(a)