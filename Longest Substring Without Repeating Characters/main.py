s = "pwwkew"
a = [] #"p", "w", "w", "k", "e", "w"
# s = "pw"

for i in range(len(s)):
    if s[i] in a:
        left = s[:i]
        print(left)
    else:
        a.append(s[i])
print(a)

