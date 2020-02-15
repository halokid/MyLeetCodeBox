package main

import (
  "testing"
)

type TreeNode struct {
  Val     int
  Left    *TreeNode
  Right   *TreeNode
}

func maxDepth(root *TreeNode) int {
  if root == nil {
    return 0
  }
  if maxDepth(root.Left) > maxDepth(root.Right) {
    return maxDepth(root.Left) + 1
  }
  return maxDepth(root.Right) + 1
}

func TestMaxDepth(t *testing.T) {

}
