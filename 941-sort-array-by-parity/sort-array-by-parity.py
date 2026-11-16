class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
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
        for j in range(len(odd)):
            res.append(odd[j])
        return res
        