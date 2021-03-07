/*
#104 二叉树的最大深度
 */

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}

use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
  pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    let mut ret = 0;
    Solution::get_node(&root, 0, &mut ret);
    ret
  }

  fn get_node(node: &Option<Rc<RefCell<TreeNode>>>, level: i32, max: &mut i32){
    if let Some(x) = node {
      Solution::get_node(&x.borrow().right, level+1, max);
      Solution::get_node(&x.borrow().left, level+1, max);
    } else {
      if level > *max { *max = level; }
    }
  }
}










