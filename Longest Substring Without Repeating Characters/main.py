s = "abcabcaa"
a = [] #"p", "w", "w", "k", "e", "w"
# s = "pw"

left = 0
right = 0

maxlen = 0

for i in range(len(s)):
    if s[i] in a:
        a = []
        a.append(s[i])
        right += 1
    elif maxlen < len(a):
        maxlen = len(a)
    
    a.append(s[i])

# while right < len(s):
#     for i in range(len(s)):
#         if s[i] in a:
#             left = i - 1
#             right = i
#             print(s[left:right])
#         a.append(s[i])

    

# print(s[6:6])

print(maxlen)
        



