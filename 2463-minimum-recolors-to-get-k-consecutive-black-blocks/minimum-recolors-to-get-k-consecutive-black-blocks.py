class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        min_o=float('inf')
        n=len(blocks)-k+1
        # if n==0:
        #     count=0
        #     for j in range(len(blocks)):
        #         if blocks[j]=="W":
        #             count+=1
        #     min_o=min(min_o,count)
        # else:
        for i in range(n):
            count=0
            for j in range(i,k+i):
                if blocks[j]=="W":
                    count+=1
            min_o=min(min_o,count)
        return min_o
        