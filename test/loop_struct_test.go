/**
循环结构体的数组
 */
package main

import (
  "fmt"
  "testing"
)

type ListNode struct {
  Val       int
  Next      *ListNode
}

func TestLoopStruct(t *testing.T)  {
  c := ListNode{3, nil}
  b := ListNode{2, &c}
  a := ListNode{1, &b}

  nodes := []ListNode{a, b, c}
  for index, res := range nodes {
    fmt.Printf("%d--------%v\n", index, res)
  }
}
