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
  i := 0
  var tmpNode *ListNode
  tmpNode = l1
  tmpNode2 := l2
  var nextAddOne int
  nextAddOne = 0
  var l3Num  []int

  //var l1s []ListNode
  //var l2s []ListNode
  for {
    if tmpNode.Next != nil {
      // add
      tmpAdd := tmpNode.Val + tmpNode2.Val + nextAddOne
      if tmpAdd >= 10 {
        tmpAdd = tmpAdd - 10
        nextAddOne = 1
      }
      fmt.Println(tmpAdd)
      l3Num = append(l3Num, tmpAdd)
      tmpNode = tmpNode.Next
      tmpNode2 = tmpNode2.Next
      i += 1
    } else {
      tmpAdd := tmpNode.Val + tmpNode2.Val + nextAddOne
      if tmpAdd >= 10 {
        tmpAdd = tmpAdd - 10
      }
      l3Num = append(l3Num, tmpAdd)
      fmt.Println(tmpAdd)
      break
    }
  }
  if len(l3Num) == 1 {
    l3Num = append(l3Num, 1)
  }
  fmt.Println(l3Num)

  var l3 []ListNode
  //var next *ListNode
  //var tmpL3 ListNode
  for i := len(l3Num)-1; i >= 0; i-- {
    var tmpL3 ListNode
    if i == len(l3Num) - 1 {
      tmpL3 = ListNode{l3Num[i], nil}
    } else {
      tmpL3 = ListNode{l3Num[i], &tmpL3}
    }
    //next := &tmpL3
    l3 = append(l3, tmpL3)
  }
  fmt.Println(l3)
  return &l3[len(l3)-1]
}

func main() {
  //l1C := ListNode{3, nil}
  //l1B := ListNode{4, &l1C}
  //l1A := ListNode{2, &l1B}

  //l2C := ListNode{4, nil}
  //l2B := ListNode{6, &l2C}
  //l2A := ListNode{5, &l2B}

  l1A := ListNode{5, nil}
  l2A := ListNode{5, nil}
  fmt.Println(addTwoNumbers(&l1A, &l2A))
}



