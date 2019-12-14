package main

import "fmt"

type ListNode struct {
  Val     int
  Next    *ListNode
}

func deleteNode(head *ListNode, node *ListNode) {
  fmt.Println("head -----------", head)
  l := &ListNode{Next: head}
  //l := &ListNode{}
  //l = head
  for l.Next != nil {
    fmt.Println("start loop ------------")
    if l.Next.Val == node.Val {
      fmt.Println("hit val -----------", l, l.Next)
      //head = head.Next
      if node.Val == head.Val {     // 如果是第一个元素
        head = head.Next
      }
      l.Next = l.Next.Next
      break
    }
    l = l.Next
  }
  fmt.Println("done loop --------------- ")
  fmt.Println(head, head.Next, head.Next.Next, head.Next.Next.Next)
  fmt.Println(l, l.Next )
}

func main() {
  l4 := ListNode{5, nil}
  l3 := ListNode{3, &l4}
  l2 := ListNode{4, &l3}
  l1 := ListNode{2, &l2}

  node := ListNode{Val: 3}
  //node := ListNode{Val: 2}
  deleteNode(&l1, &node)
}