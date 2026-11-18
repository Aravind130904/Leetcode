class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        d=arr[1]-arr[0]
        res=False
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]==d:
                res=True
            else:
                return False
        return res