def maxProfit(prices):
    if len(prices) < 2:
        print('false')
    index = len(prices)
    min_left = []
    minLeft = 0
    difference = []
    for i in range(len(prices)):
        if i == 0:
            min_left.append(prices[i])
            minLeft = prices[i]
        elif prices[i] >= minLeft:
            min_left.append(minLeft)
        elif prices[i] < minLeft:
            min_left.append((prices[i]))
            minLeft = prices[i]

    for i in range(len(prices)):
        difference.append(prices[i] - min_left[i])
    max_profile = max(difference)
    max_point = difference.index(max(difference))
    max_price = prices[max_point]
    min_price = max_price - max_profile
    min_point = min_left.index(min_price)
    print(" 最大利润：", max_profile, "\n", "最佳买点：", min_point, "\n", "最佳卖点：", max_point, "\n", "最佳买点值：", min_price,
          "\n", "最佳卖点值：", max_price)