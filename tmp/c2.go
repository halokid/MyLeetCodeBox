package main

import "fmt"

func delNode(node *ListNode) {
  node.Val = node.Next.Val
  node.Next = node.Next.Next
}

func main() {
  l4 := ListNode{5, nil}
  l3 := ListNode{3, &l4}
  l2 := ListNode{4, &l3}
  l1 := ListNode{2, &l2}

  head := &l1
  printListnode(head)
  fmt.Println("--------------------------")
  delNode(&l3)
  printListnode(head)

}

func printListnode(head *ListNode) {
  for head.Next != nil {
    fmt.Println(head)
    head = head.Next
  }
  fmt.Println(head)
}

