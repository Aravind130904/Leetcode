class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        n=len(nums)
        result=[]
        for i in range(0,n):
            if nums[i]==target:
                result.append(i)
        return result