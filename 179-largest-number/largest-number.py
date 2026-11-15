class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        arr=[]
        for num in nums:
            arr.append(str(num))
        n=len(arr)

        for i in range(n):
            for  j in range(n-i-1):
                if arr[j]+arr[j+1]<arr[j+1]+arr[j]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        res=''
        for num in arr:
            res+=num
        if res[0]=='0':
            return '0'
        return res