class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        common=[]

        for n1 in nums1:
            for n2 in nums2:
                if n1==n2:
                    if n1 not in common:
                        common.append(n1)
        return common
        