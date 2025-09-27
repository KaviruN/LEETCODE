s = "pwwkew"
a = [] #"p", "w", "w", "k", "e", "w"
# s = "pw"

for i in range(len(s)):
    if s[i] in a:
        left = s[:i]
        a.remove(s[i])
    a.append(s[i])


