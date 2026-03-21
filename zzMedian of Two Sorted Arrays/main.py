# nums1 = [23, 26, 31, 35]
# nums2 = [3, 5, 7, 9, 11, 16]

nums1 = [1, 3, 8, 9, 15]
nums2 = [7, 11, 18, 19, 21, 25]


def findMedia(x, y):
    start = 0
    end = len(x) #x want to smaller one in lenth

    while start <= end:
        partition_x = (start + end) // 2

        partition_y = (len(x) + len(y) + 1) // 2 - partition_x

        leftx = x[:partition_x]
        rightx = x[partition_x:]
        lefty = y[:partition_y]
        righty = y[partition_y:]

        max_leftx = max(leftx, default=float('-inf')) #handel inf mean the 0s 
        min_rightx = min(rightx, default=float('inf'))
        max_lefty = max(lefty, default=float('-inf'))
        min_righty = min(righty, default=float('inf'))

        cond1 = max_leftx <= min_righty
        cond2 = max_lefty <= min_rightx
        if cond1 and cond2:
            if (len(x) + len(y)) % 2 == 1:
                median = max(max_leftx, max_lefty)
                return median #odd
            else:
                median = (max(max_leftx, max_lefty) + min(min_rightx, min_righty)) / 2 #even
                return median
            
        elif max_leftx > min_righty:
            end = partition_x - 1
        
        else:
            start = partition_x + 1
            

        

if len(nums2) >= len(nums1):
    # print(findMedia(nums1, nums2))
    findMedia(nums1, nums2)

else:
    findMedia(nums2, nums1)
    # print(findMedia(nums2, nums1))









