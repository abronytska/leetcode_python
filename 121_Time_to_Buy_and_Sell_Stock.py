def maxProfit(prices):
    # max_bit = 0
    # for i in range(len(prices)):
    #     for j in range(len(prices)):
    #         if i < j and max_bit < prices[j] - prices[i]:
    #             max_bit = prices[j] - prices[i]
    # return max_bit
    minprice = max(prices)
    maxprofit = 0
    for i in range(len(prices)):
        if prices[i] < minprice:
            minprice = prices[i]
        elif prices[i] - minprice > maxprofit:
            maxprofit = prices[i] - minprice

    return maxprofit


# print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 1, 5, 2, 6, 14]))
