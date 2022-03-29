package pkg;

// todo: reference URL  https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/intersection-of-two-linked-lists-shuang-zhi-zhen-l/

// Definition for singly-linked list.
public class IntersectList {

  public class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
      val = x;
      next = null;
    }
  }

  public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    ListNode A = headA, B = headB;
    while (A != B) {
      A = A != null ? A.next : headB;
      B = B != null ? B.next : headA;
    }
    return A;
  }
}





