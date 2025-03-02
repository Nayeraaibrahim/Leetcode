class Solution(object):
    def mergeArrays(self, nums1, nums2):
        res = []
        i,j=0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0],nums1[i][1]+nums2[j][1]])
                i+=1
                j+=1
            elif nums1[i][0]<nums2[j][0]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        res.extend(nums1[i:])
        res.extend(nums2[j:])
        return res




        