class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res=[-1]*len(nums1)
        d={}
        st=[]
        for i in nums2:
            while(st and i>st[-1]):
                d[st.pop()]=i
                
            st.append(i)

        for i in range(len(nums1)):
            if nums1[i] in d:
                res[i]=d[nums1[i]]
        return res