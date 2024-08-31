from typing import List


class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    left_point = 0
    right_point = 1

    while right_point < len(nums):
      if nums[left_point] == nums[right_point]:
        right_point += 1
      else:
        nums[left_point + 1] = nums[right_point]
        left_point += 1
        right_point += 1
      print('left_point: ', left_point, ', right_point: ', right_point)

    print(nums)
    # return len(nums)
    return left_point + 1

if __name__ == '__main__':
  sl = Solution()
  # nums = [1, 1, 2]
  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
  new_nums = sl.removeDuplicates(nums)
  print(new_nums)
