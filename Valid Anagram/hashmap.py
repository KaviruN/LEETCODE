s = "anagram"
t = "nagacam"

def isAnagram(s, t):
    sCount, tCount = {}, {}

    for i in range(len(s)):
        sCount[s[i]] += 1

    print(sCount)  


# a = {}


# a['a'] = 1

# print(a)