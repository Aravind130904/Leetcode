class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res=[0]*len(temperatures)
        st=[]
        for i in range(len(temperatures)):
            while(st and temperatures[i]>temperatures[st[-1]]):
                prev=st.pop()
                res[prev]=i-prev
            st.append(i)
        return res