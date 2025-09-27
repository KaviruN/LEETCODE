s = "pww"
a = [] #"p", "w", "w", "k", "e", "w"
# s = "pw"

left = 0
right = 0

maxlen = 0

for i in range(len(s)):
    if s[i] in a:
        left = i - 1
        right = i
    a.append(s[i])

print(s[left:right])
        



