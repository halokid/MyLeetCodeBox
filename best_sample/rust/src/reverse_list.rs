/*
#206 反转链表
 */

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  val:    i32,
  next:   Option<Box<ListNode>>     // 有可能是null， 所以要用option
}

impl ListNode {

  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      val:    val,
      next:   None,
    }
  }
}

impl Solution {
  pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    if head.is_none() {
      return None;
    }
    let mut prev: Option<Box<ListNode>> = None;
    let mut curr: Option<Box<ListNode>> = head;
    while curr.is_some() {
      let mut node = curr.take().unwrap();
      curr = node.next;
      node.next = prev;
      prev = Some(node);
    }
    prev
  }
}


