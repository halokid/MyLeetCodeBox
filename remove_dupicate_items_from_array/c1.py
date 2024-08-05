from typing import List


class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    i = 0
    j = 1

    while j < len(nums):
      if nums[i] == nums[j]:
        j += 1
      else:
        nums[i + 1] = nums[j]
        i += 1
        j += 1
      print('i: ', i, ', j: ', j)

    print(nums)
    # return len(nums)
    return i+1

if __name__ == '__main__':
  sl = Solution()
  # nums = [1, 1, 2]
  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
  new_nums = sl.removeDuplicates(nums)
  print(new_nums)
