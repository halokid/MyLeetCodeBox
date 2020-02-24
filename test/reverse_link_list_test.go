package main

import (
  "fmt"
  "testing"
)

type ListNode struct {
  Val   int
  Next  *ListNode
}

func reverserList(head *ListNode) *ListNode {
  i := 0
  for {
    if i > 2 {
      break
    }
    fmt.Printf("%+v\n", head)
    head.Next.Next = head
    head = head.Next
    i++
  }
  return head
}

func TestReverseList(t *testing.T) {
  n3 := &ListNode{3, nil}
  n2 := &ListNode{2, n3}
  n1 := &ListNode{1, n2}

  reverserList(n1)
}