package main

import "fmt"

/**
两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

 */

 type ListNode struct {
   Val    int
   Next   *ListNode
 }

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
  //var l *ListNode = &ListNode{}
  l := &ListNode{}
  // fixme: 改变pre就是改变l， 所以最后返回 l  是
  pre := l
  carry := 0
  for l1 != nil || l2 != nil {
    pre.Next = &ListNode{}      // 建立一个空的 ListNode 为前一个的Next,  定义pre的Next
    p := pre.Next         // fixme: 理解的关键， 这个是当前的节点
    x := 0
    y := 0
    if l1 != nil {
      x = l1.Val
      l1 = l1.Next      // 假如链表的Next不为空，则继续循环
    }

    if l2 != nil {
      y = l2.Val
      l2 = l2.Next
    }

    p.Val = (x + y + carry) % 10    //  赋值了 pre的 Val
    carry = (x + y + carry) / 10      // 返回除以10的整数， 为1
    pre = p       // fixme: 理解的关键， 位置1: 下一个循环的前一个等于当前循环已经算出的p, 定义pre的Val
    fmt.Println("l xx  in func -------------- ", l)
  }

  // 两个相加的单链表都循环运算完成， 假如最后一个Next相加大于10， 则生成的链表最后一位val 为 carry， Next为空
  if carry != 0 {
    pre.Next = &ListNode{Val: carry}
  }

  fmt.Println("l in func -------------- ", l)
  fmt.Println("l Next in func -------------- ", l.Next)
  fmt.Println("l xx n n   in func -------------- ", l.Next.Next)
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
  fmt.Printf("%v+\n", ln)
  fmt.Printf("%v\n", ln)
  fmt.Printf("%t\n", ln)

  fmt.Println("--------------------------")
  fmt.Println(ln)         // 输出 &{8 0xc00008e040}
  fmt.Println(ln.Next)
  fmt.Println(ln.Next.Next)
}




