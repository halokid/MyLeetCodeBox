package main

import (
  "fmt"
  "golang.org/x/text/currency"
  "log"
  "testing"
)

type ListNode struct {
  Val   int
  Next  *ListNode
}

func reverserList1(head *ListNode) *ListNode {
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

func reverserList(currHead *ListNode) *ListNode {
  // 迭代法
  var prevHead, next *ListNode
  for currHead != nil {
    // 以 1节点到2节点作为分析， 重点是每一个循环要设置好 prevHead, head 两个变量
    next = currHead.Next      // 1节点的next为2
    currHead.Next = prevHead   // 设置1节点的next为一个空的newHead
    prevHead = currHead        // newHead承接当前的节点
    currHead = next           // 设置当前head为2节点， 下一步循环开始置换2，3节点，一直到next为空（也就是最后一个元素）终于
  }
  return prevHead
}

func reverserListRec(currHead *ListNode) *ListNode {
  if currHead == nil || currHead.Next == nil {
    return currHead
  }
  newHead := reverserListRec(currHead.Next)
  currHead.Next.Next 
}

func TestReverseList(t *testing.T) {
  n3 := &ListNode{3, nil}
  n2 := &ListNode{2, n3}
  n1 := &ListNode{1, n2}

  reverserList1(n1)
  log.Println("-----------------------")
  reverserList(n1)
}