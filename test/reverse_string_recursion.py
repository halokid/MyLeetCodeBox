# coding=utf-8


class Solution:
  def reverseString(self, s):
    def helper(left, right):
      if left < right:
        s[left], s[right] = s[right], s[left]
        # helper(left + 1, right - 1)

    helper(0, len(s) - 1)


class Solution2:
  def reverseString(self, s):
    left, right = 0, len(s) - 1
    while left < right:
      s[left], s[right] = s[right], s[left]
      left, right = left + 1, right - 1

if __name__ == "__main__":
  s = "hello"
  print(s[1])
  # s[2] = "x"
  '''
  sl = Solution()
  sl.reverseString(s)
  print(s)
  '''
