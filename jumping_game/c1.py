from typing import List

DEBUG = True


def debug(*s):
  if DEBUG:
    print(*s)


def find_last_zero(nums: List[int]):
  zero_idx = 0
  for idx, num in enumerate(nums):
    if num == 0:
      zero_idx = idx
  return zero_idx


class SolutionOld:
  def canJump(self, nums: List[int]) -> bool:
    debug("nums -->>>", nums)
    nums_len = len(nums)
    if nums_len == 1:
      return True

    for idx, num in enumerate(nums):
      if num == 0 and nums[idx - 1] == 1 and idx < nums_len - 2:
        return False

    if 0 in nums:
      # zero_index = nums.index(0)
      zero_index = find_last_zero(nums)
      while zero_index > 0:
        debug("zero_index -->>>", zero_index)
        if nums[zero_index - 1] >= nums_len - zero_index:
          return True
        else:
          zero_index -= 1
      return False
    else:
      return True


class Solution:
  def canJump(self, nums: List[int]) -> bool:
    reach = 0

    for i, num in enumerate(nums):
      if i > reach:
        return False
      reach = max(i + num, reach)

    return True


if __name__ == "__main__":
  # nums = [2, 3, 1, 1, 4]
  # nums = [3, 2, 1, 0, 4]
  # nums = [0]
  # nums = [2, 0, 0]
  # nums = [1, 0, 1, 0]
  nums = [1, 1, 2, 2, 0, 1, 1]

  solu = Solution()
  res = solu.canJump(nums)
  debug('res -->>>', res)
