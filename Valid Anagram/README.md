# Valid Anagram

## Problem Explanation

**Anagram means:**
- Two strings are anagrams if they contain the same characters with the same frequency
- Length must be the same: `len(s) == len(t)`
- All characters from `t` must be in `s` with the same count

**Example:**
```
s = "anagram", t = "nagaram"
- Both have length 7 ✓
- Characters count:
  anagram = a(3) + n(1) + g(1) + r(1) + m(1)
  nagaram = n(1) + a(3) + g(1) + r(1) + m(1)
- Same letters, same count ✓ → Valid Anagram
```

**Another way to think:**
```
nagaram = naaagrm (sorted by frequency)
anagram = aaanmgr (sorted by frequency)
Same letters, same count!
```

## Solutions

### Approach 1: Sorting Method
**File:** `main.py`
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(1) or O(n) depending on sorting implementation
- **Method:** Sort both strings and compare

### Approach 2: HashMap/Dictionary Method  
**File:** `hashmap.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Method:** Count character frequency using dictionaries
- **Key Insight:** Use `dict.get(key, 0) + 1` to count characters