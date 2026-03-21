nums1 = [1,3]
nums2 = [2]


numarray = nums1 + nums2

numarray = sorted(numarray)

arraylen = len(numarray)

if arraylen % 2 == 1:
    median = numarray[(arraylen // 2)]

else:
    median = (numarray[(arraylen // 2 - 1)] + numarray[(arraylen // 2)]) / 2

 