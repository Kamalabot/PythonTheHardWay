problem = """You are given an array prices where prices[i] is the
price of a given stock on the ith day.You want to maximize your profit
by choosing a single day to buy one stock and choosing a different
day in the future to sell that stock. Return the maximum profit you can
achieve from this transaction. If you cannot achieve any profit, return 0."""

approach = """
- each price point is substracted with only the future
    a) Traverse the price 
    b) calculate the profit with all the future prices, 
    c) and store in profit list 
    d) id max value of each list
    e) id max in the days and return
    if not then return 0 
- look at the biggest txn and return the days
"""


# below solution timelimit exceeded
def profit(priceList):
    if len(priceList) == 1:
        return 0
    days_max = {}
    for ind in range(len(priceList) - 1):
        prof = []
        for n in priceList[ind+1:]: 
            prof.append(n - priceList[ind])
        days_max[ind] = max(prof)
    print(days_max)
    output = max(list(days_max.values()))
    return output if output > 0 else 0


def maxProfit(prices):
# Initialize two variables, minPrice to track the minimum price of the stock so far and maxProfit to track the maximum profit so far.
    min_price = 1
    max_profit = 0
# Iterate through the array of prices.
    for price in prices:
# For each price, check if it is smaller than the current minPrice. If it is, update minPrice.
        if price < min_price:
            min_price = price
# If the price minus the minPrice is greater than the current maxProfit, update maxProfit.
        inter_prof = price - min_price
        if inter_prof > max_profit:
            max_profit = inter_prof
# Finally, return the maxProfit.
    return max_profit


class Solution:
    def maxProfit(self, prices) -> int:
        maxGap = 0  # initialize maxgap variable
        left, right = 0, 1  # initialize left and right 0, 1
        while right < len(prices):  # while the right is less than list
            if prices[left] < prices[right]:
                # check if price @ left < price @ right
                maxGap = max(maxGap, prices[right] - prices[left])
                #  get the max of maxGap & diff of right - left
                right += 1  # increment the right by one
            else:
                # price @ left > price @ right
                left, right = right, right + 1
                # shift to the next pair

        return maxGap

prices = [7, 1, 5, 3, 6, 4]
# print(maxProfit(prices))
sol = Solution()
print(sol.maxProfit(prices))
# Output: 5
# Explanation: Buy on day 2 (price = 1) 
# and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is 
# not allowed because you must buy before you sell.

prices = [7, 6, 4, 3, 1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
# print(profit(prices))
# print(maxProfit(prices))
print(sol.maxProfit(prices))