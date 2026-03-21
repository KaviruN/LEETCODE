

s = "bbbbb"

a = []       
left = 0
maxlen = 0

for right in range(len(s)):
   
    while s[right] in a:
        a.pop(0)  
        left += 1
    
    a.append(s[right])  
    maxlen = max(maxlen, len(a))  

print(maxlen)  







