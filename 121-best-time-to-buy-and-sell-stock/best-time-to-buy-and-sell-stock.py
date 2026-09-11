class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # l,r =0,1
        # maxP=0
        # while r<len(prices):
        #     if prices[l]<prices[r]:
        #         profit=prices[r]-prices[l]
        #         maxP=max(maxP,profit)
        #     else:
        #         l=r
        #     r+=1
        # return maxP 
        # min_price=float('inf')
        # day=0
        # for i in range(len(prices)):
        #     if(prices[i]<min_price):
        #         min_price=prices[i]
        #         day=i
        # max_profit=0
        # for j in range(day+1,len(prices)):
        #     if(prices[i]>min_price and j>day):
        #         max_profit=max(max_profit,profit[j]-min_price)
        # return max_profit
        min_price=float('inf')
        max_price=0

        for price in prices:
            min_price=min(min_price,price)
            max_price=max(max_price,price-min_price)
        return max_price








