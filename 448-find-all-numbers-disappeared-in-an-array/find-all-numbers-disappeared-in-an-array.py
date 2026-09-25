class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        d=[]
        s=set(nums)
        for i in range(1,n+1):
            if i not in s:
                d.append(i)

        return d
        