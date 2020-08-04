class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = []

        for i, price in enumerate(prices):
            if i == 0:
                continue

            j = i
            while price >= prices[j - 1] and j > 0:

                max_profit.append(price - prices[j - 1],)
                j -= 1
            if j == i:
                max_profit[i] = [price]
            else:
                max_profit[i] = [price - prices[j], j, i]

        max_p = self.choose_purchase(max_profit)

        return max_p

    def choose_purchase(self, max_profit):
        final_purchases = []
        for purchase in max_profit:
            if len(purchase) == 3:
                final_purchases.append(purchase)

        sorted_purchases = sorted(final_purchases, key=lambda s: s[2])
        print(sorted_purchases)
        if sorted_purchases:
            max_profit = sorted_purchases[-1][0]
            max_profit_buy_id = sorted_purchases[-1][1]
            j = len(sorted_purchases) - 2
            while j >= 0:
                if sorted_purchases[j][2] < max_profit_buy_id:
                    max_profit += sorted_purchases[j][0]
                    return max_profit
                j -= 1
            return max_profit
        else:
            return 0

s = Solution()
print(s.maxProfit([1,2,4,2,5,7,2,4,9,0]))
print(s.maxProfit([3,2,6,5,0,3]))
print(s.maxProfit([2,1,2,0,1]))
print(s.maxProfit([7,6,4,3,1]))

