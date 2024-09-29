import time
from typing import List

DEBUG = True


def debug(*s):
  if DEBUG:
    print(*s)


class Solution:
  def jump_bad1(self, nums: List[int]) -> int:
    position = len(nums) - 1
    jump = 0
    while position > 0:
      debug('out position -->>>', position)
      i = 0
      while i < position:
        if i + nums[i] >= position:
          debug('get i -->>>', i)
          position = i
          jump += 1
          debug('get new position -->>>', position)
          break
        i += 1

    return jump

  def jump(self, nums: List[int]) -> int:
    debug('nums -->>>', nums)
    nums_len = len(nums)
    end = 0
    new_can_reach_max = 0
    jumps = 0

    i = 0
    while i < nums_len - 1:
      new_can_reach_max = max(new_can_reach_max, i + nums[i])
      debug('i --->', i, ', new_can_reach_max -->>>', new_can_reach_max)
      if i == end:
        end = new_can_reach_max
        debug('set end -->>>', end)
        jumps += 1
      i += 1
      debug("-------------------")
    return jumps



if __name__ == "__main__":
  start = time.time()
  nums = [2, 3, 1, 1, 4]
  # nums = [2, 3, 0, 1, 4]
  # nums = [2, 1, 1, 1, 4]
  solu = Solution()
  res = solu.jump(nums)
  print(res)

  cost = time.time() - start
  debug('cost -->>>', cost)
