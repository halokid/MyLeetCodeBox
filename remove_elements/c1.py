from typing import List

class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    left = 0
    for item in nums:
      if item != val:
        nums[left] = item
        left += 1
    return left

