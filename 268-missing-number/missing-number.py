class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        # ans=n
        # for i in range(len(nums)):
        #     ans=ans^i^nums[i]
        # return ans
        sum1=(n*(n+1))//2
        s=0
        for num in nums:
            s+=num
        return (sum1-s)