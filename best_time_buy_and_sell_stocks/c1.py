from typing import List

DEBUG = True

def debug(*s):
  if DEBUG:
    print(*s)

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    nums_len = len(nums)
    left, right, answer = [0] * nums_len, [0] * nums_len, [0] * nums_len

    left[0] = 1
    for i in range(1, nums_len):
      debug(left[i - 1], nums[i - 1])
      left[i] = left[i - 1] * nums[i - 1]
    debug("left -->>>", left)

    right[nums_len - 1] = 1
    for i in range(1, nums_len):
      debug(right[nums_len - 1], nums[nums_len - i])
      right[nums_len - 1 - i] = right[nums_len - i] * nums[nums_len - i]
    debug("right -->>>", right)

    res = [0] * nums_len
    for i in range(0, nums_len):
      res[i] = left[i] * right[i]
    return res


if __name__ == "__main__":
  nums = [1, 2, 3, 4]
  solu = Solution()
  res = solu.productExceptSelf(nums)
  debug('res -->>>', res)


