package main

import (
  "fmt"
)

type ListNode struct {
  Val     int
  Next    *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
  var l *ListNode = &ListNode{}
  pre := l
  carry := 0
  for l1 != nil || l2 != nil {
    fmt.Println("pre ----------", pre)
    pre.Next = &ListNode{}
    p := pre.Next
    x := 0
    y := 0
    if l1 != nil {
      x = l1.Val
      l1 = l1.Next
    }

    if l2 != nil {
      y = l2.Val
      l2 = l2.Next
    }

    p.Val = (x + y + carry) % 10
    fmt.Println("val ----------", p.Val)
    carry = (x + y + carry) / 10
    pre = p
    fmt.Println("p ----------", p)
    fmt.Println("++++++++++++++++++++++++++++++++++++++")
  }

  if carry != 0 {
    pre.Next = &ListNode{Val: carry}
  }
  return l.Next
}

func main() {
  l3 := ListNode{3, nil}
  l2 := ListNode{4, &l3}
  l1 := ListNode{2, &l2}

  lx3 := ListNode{4, nil}
  lx2 := ListNode{6, &lx3}
  lx1 := ListNode{5, &lx2}

  ln := addTwoNumbers(&l1, &lx1)
  fmt.Println(ln)
  fmt.Println(ln.Next)
  fmt.Println(ln.Next.Next)
}


