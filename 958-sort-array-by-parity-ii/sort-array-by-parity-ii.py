class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even=[]
        odd=[]
        res=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        for i in range(len(even)):
            res.append(even[i])
            res.append(odd[i])
        return res