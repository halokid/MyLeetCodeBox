/**
两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
 */
package main

import "fmt"

type ListNode struct {
  Val     int
  Next    *ListNode
}

func reverse(s []int) []int {
  for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
    s[i], s[j] = s[j], s[i]
  }
  return s
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
  l1Num := []int{l1.Val}
  l2Num := []int{l2.Val}
  //var tmpNode *ListNode
  tmpNode1 := l1
  tmpNode2 := l2
  for {
    //tmpNode = l1
    if tmpNode1.Next != nil && tmpNode2.Next != nil {
      tmpNode1 = tmpNode1.Next
      tmpNode2 = tmpNode2.Next
      l1Num = append(l1Num, tmpNode1.Val)
      l2Num = append(l2Num, tmpNode2.Val)
    } else if tmpNode1.Next == nil && tmpNode2.Next == nil {
      //l1Num = append(l1Num, tmpNode1.Val)
      //l2Num = append(l2Num, tmpNode2.Val)
      break
    }
  }
  fmt.Println(l1Num)
  fmt.Println(l2Num)

  // loop add
  var l3Num []int
  nextAdd := 0
  for index, l1Item := range l1Num {
    tmpNum := l1Item + l2Num[index]
    if tmpNum >= 10 {
      if nextAdd == 0 {
        nextAdd = 1
        tmpNum = tmpNum - 10
      } else {
        tmpNum = tmpNum - 10 + 1
      }
      l3Num = append(l3Num, tmpNum)
    } else {
      l3Num = append(l3Num, tmpNum + nextAdd)
      nextAdd = 0
    }
  }
  if len(l3Num) == 1 &&  l1Num[0]+l2Num[0] >= 10 {
    l3Num = append(l3Num, 1)
  }
  /**
  else if len(l3Num) == 1 &&  l1Num[0]+l2Num[0] < 10 {
    l3Num = []int{0}
  }
  **/
  fmt.Println(l3Num)

  fmt.Println("----------------------------------------")

  var l3 []ListNode
  //var l3Item  ListNode
  var tmpItem *ListNode
  for i := len(l3Num)-1; i >= 0; i-- {
    if tmpItem == nil {
      //println("xx")
      l3Item := ListNode{l3Num[i], nil}
      tmpItem = &l3Item
      l3 = append(l3, l3Item)
    } else {
      //println("yy")
      l3Item := ListNode{l3Num[i], tmpItem}
      tmpItem = &l3Item
      l3 = append(l3, l3Item)
    }
  }
  fmt.Printf("%v\n", l3)
  return &l3[len(l3Num)-1]
}

func main() {
  //l1C := ListNode{3, nil}
  //l1B := ListNode{4, &l1C}
  //l1A := ListNode{2, &l1B}

  l1A := ListNode{1, nil}

  //l2C := ListNode{4, nil}
  //l2B := ListNode{6, &l2C}
  //l2A := ListNode{5, &l2B}

  l2A := ListNode{8, nil}

  l3 := addTwoNumbers(&l1A, &l2A)
  fmt.Printf("%v\n", l3)
  fmt.Printf("%v\n", *l3)
  fmt.Printf("%v\n", l3.Next)
  fmt.Printf("%v\n", *l3.Next)
  fmt.Printf("%v\n", l3.Next.Next)
  fmt.Printf("%v\n", *l3.Next.Next)
}




