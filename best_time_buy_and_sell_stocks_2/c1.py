from typing import List

DEBUG = False
def debug(*s):
  if DEBUG:
    print(*s)

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    i = 0

    for _ in prices:
      debug(i)
      if i == 0:
        i += 1
        continue
      if prices[i] > prices[i - 1]:
        debug(prices[i], prices[i - 1])
        profit += prices[i] - prices[i - 1]
      i += 1
    return profit


if __name__ == "__main__":
  prices = [7, 1, 5, 3, 6, 4]
  solu = Solution()
  p = solu.maxProfit(prices)
  print(p)
