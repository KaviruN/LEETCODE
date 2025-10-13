s = "racecar"
t = "carrabe"

def a(s,t):
    sset, tset = {}, {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        sset[s[i]] = sset.get(s[i], 0) + 1 #{'r': 2, 'a': 2, 'c': 2, 'e': 1} 
    for j in range(len(t)):
        tset[t[j]] = tset.get(t[j], 0) + 1 #{'c': 2, 'a': 2, 'r': 2, 'e': 1}

    for k in sset:
        if sset[k] != tset.get(k, 0):
            return False
    return True



print(a(s,t))