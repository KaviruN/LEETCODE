# Median of Two Sorted Arrays

## Binary Search Algorithm Notes

**Key Formulas:**
- If array is **even**: `median = avg(max(leftx,lefty), min(rightx,righty))`
- If array is **odd**: `median = max(leftx, lefty)`

**Algorithm Steps:**
1. Ensure `len(x) <= len(y)` (x is the smaller array)
2. Initialize: `start = 0`, `end = len(x)`
3. Calculate partitions:
   - `Partitionx = (start + end) / 2`
   - `Partitiony = (len(x) + len(y) + 1) / 2 - Partitionx`

**Binary Search Logic:**
```
Found (correct partition):
    maxLeftX <= minRightY
    maxLeftY <= minRightX
    → Calculate and return median

else if maxLeftX > minRightY:
    move towards left in X
    → end = Partitionx - 1

else:
    move towards right in X
    → start = Partitionx + 1
```

**Files:**
- `aproch1.py` - Simple merge and sort approach
- `main.py` - Binary search approach (optimal)