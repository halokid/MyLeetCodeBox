from typing import List

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
      nums.insert(0, nums.pop())

if __name__ == "__main__":
  sl1 = [1,2,3,4,5,6,7]
  sl1_len = len(sl1)
  k = 3
  print(sl1[:-k])
  print(sl1[-k:])
  print(sl1[-k:] + sl1[:-k])

  solu = Solution()
  solu.rotate(sl1, k = k)


