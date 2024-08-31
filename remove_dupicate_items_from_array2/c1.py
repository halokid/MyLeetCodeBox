from typing import List


class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 2:
      return n

    left_point = 2
    right_point = 2
    while right_point < n:
      if nums[left_point - 2] != nums[right_point]:
        nums[left_point] = nums[right_point]
        left_point += 1

      right_point += 1

    return left_point


sl = [0, 0, 1, 1, 1, 1, 2, 3, 3]
rosl = Solution()
lx = rosl.removeDuplicates(sl)
print(lx)
