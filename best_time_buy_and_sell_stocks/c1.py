from typing import List

DEBUG = True


def debug(*s):
  if DEBUG:
    print(*s)


# TODO:  this way if the list has some element duplicate,  will fail in case
class Solution:
  def maxProfit_c1(self, prices: List[int]) -> int:
    old_prices = prices.copy()
    debug('old_price 1 -->>>', old_prices)

    prices.sort()
    debug('sort_prices -->>>', prices)
    debug('old_price 2 -->>>', old_prices)

    left = 0
    right = len(prices) - 1
    debug('prices[left] -->>>', prices[left], old_prices.index(prices[left]))
    debug('prices[right] -->>>', prices[right], old_prices.index(prices[right]))

    while left < right:
      if old_prices.index(prices[left]) < old_prices.index(prices[right]):
        debug('1:', left, right)
        return prices[right] - prices[left]
      else:
        debug('left 1:', left)
        left += 1

    left = 0
    right = len(prices) - 1
    while left < right:
      if old_prices.index(prices[left]) < old_prices.index(prices[right]):
        debug('2:', left, right)
        return prices[right] - prices[left]
      else:
        debug('right 1:', right)
        right -= 1

    return 0

  def maxProfit(self, prices: List[int]) -> int:
    min_num = prices[0]
    max_profit = 0

    for p in prices:
      if p < min_num:
        min_num = p
      elif p - min_num > max_profit:
        max_profit = p - min_num
    return max_profit


if __name__ == "__main__":
  # minus (7-1) for each one:  1, -5, -1, -3, 0, -2
  # prices = [7, 1, 5, 3, 6, 4]
  # prices = [2, 1, 2, 0, 1]
  prices = [7, 6, 4, 3, 1]
  # debug('index 2 -->>>', prices.index(2, 0, len(prices)))
  # print(price.index(5))
  solu = Solution()
  print(solu.maxProfit(prices))

  # --------------------------------------
  # minus (8-1) for each one:  0, -6, -2, -4, 1, -3
  # price = [7, 1, 5, 3, 8, 4]
