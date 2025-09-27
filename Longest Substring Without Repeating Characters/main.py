s = "pww"
a = [] #"p", "w", "w", "k", "e", "w"
# s = "pw"

left = []
right = []

maxlen = 0

for i in range(len(s)):
    if s[i] in a:
        left.append(s[:i])
        right.append(s[i:])
        print(left, right)
        
    else:
        a.append(s[i])
        maxlen += 1


