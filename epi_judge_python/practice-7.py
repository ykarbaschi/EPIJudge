
def merge(nums1, nums2):
    res = []
    i = 0
    j= 0
    k = 0

    while i < len(nums1) and j <len(nums2):
        if nums1[i] < nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
        k += 1

    while i < len(nums1):
        res.append(nums1[i])
        i += 1
        k += 1

    while j < len(nums2):
        res.append(nums2[j])
        j += 1
        k += 1

    return res

print(merge([1,2,3],[2,3,4]))