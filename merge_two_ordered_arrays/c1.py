from typing import List

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    n = len(nums)
    check_len = int(n / 2)    # get smaller int

    eles_map = dict()
    for num in nums:
      if num not in eles_map.keys():
        eles_map[num] = 1
      else:
        eles_map[num] += 1

      if eles_map[num] > check_len:
        return num

    # print(eles_map)



if __name__ == "__main__":
  nums = [2, 2, 1, 1, 1, 2, 2]
  sl = Solution()
  print(sl.majorityElement(nums))

