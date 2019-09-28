package main

import (
  "fmt"
)

type ListNode struct {
  Val     int
  Next    *ListNode
}

/**
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
  l3 := ListNode{0, nil}
  p := l1
  q := l2
  curr := &l3
  carry := 0
  for {
    var x, y int

    if p == nil && q == nil {
      break
    }

    if p != nil {
      x = p.Val
    } else {
      x = 0
    }

    if q != nil {
      y = q.Val
    } else {
      y = 0
    }

    sum := x + y + carry
    carry = sum / 10      // 如果 carry大于10， 则carry为1
    curr.Next = &ListNode{sum % 10, nil}
    curr = curr.Next

    if p != nil { p = p.Next }
    if q != nil { q = q.Next }
  }

  if carry > 0 {
    curr.Next = &ListNode{carry, nil}
  }

  return l3.Next      // 第一次赋值curr 的时候改了 l3 的next， 后面就是直接改 curr本身的了，当然也是改l3链上的，所以返回 l3.Next 是可以一直追下去的
}

func main() {
  //l1C := ListNode{3, nil}
  //l1B := ListNode{4, &l1C}
  //l1A := ListNode{2, &l1B}

  //l2C := ListNode{4, nil}
  //l2B := ListNode{6, &l2C}
  //l2A := ListNode{5, &l2B}

  l1A := ListNode{3, nil}
  l2A := ListNode{5, nil}
  //fmt.Println(addTwoNumbers(&l1A, &l2A))

  l3 := addTwoNumbers(&l1A, &l2A)
  var curr *ListNode
  curr = l3
  for {
    if curr.Next == nil {
      fmt.Println(curr)
      break
    }

    if curr.Next != nil {
      fmt.Println(curr)
      curr = curr.Next
    }
  }
}



