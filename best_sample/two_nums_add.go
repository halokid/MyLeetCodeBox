package main
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
  var l *ListNode = &ListNode{}
  pre := l
  carry := 0
  for l1 != nil || l2 != nil {
    pre.Next = &ListNode{}      // 建立一个空的 ListNode 为前一个的Next
    p := pre.Next
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

    p.Val = (x + y + carry) % 10
    carry = (x + y + carry) / 10      // 返回除以10的整数， 为1
    pre = p       // 1 下一个循环的前一个等于当前循环已经算出的p
  }

  // 两个相加的单链表都循环运算完成， 假如最后一个Next相加大于10， 则生成的链表最后一位val 为 carry， Next为空
  if carry != 0 {
    pre.Next = &ListNode{Val: carry}
  }

  return l.Next
}





