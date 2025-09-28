s = "anagram"
t = "nagacam"



def cheackAnagram(s, t):
    s = sorted(s)
    t = sorted(t)
    
    if s == t:
        return True

    else:
        return False
    
print(cheackAnagram(s, t))