# coding=utf-8

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    if root is None:
      return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1



if __name__ == "__main__":
  r3 = TreeNode(3)

  r3Sub4 = TreeNode(4)

  r20Sub15 = TreeNode(15)
  r20Sub7 = TreeNode(7)

  r3Sub20 = TreeNode(20)
  r3Sub20.left = r20Sub15
  r3Sub20.right = r20Sub7

  r3.left = r3Sub4
  r3.right = r3Sub20

  s = Solution()
  print(s.maxDepth(r3))



