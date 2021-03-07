/*
#1342 将数字变成 0 的操作次数
 */

impl Solution {
  pub fn number_of_steps(num: i32) -> i32 {
    let mut num = num;
    let mut ret = 0;

    while num != 0 {
      match num % 2 {
        0 => num = num / 2,
        _ => num = num - 1,
      }
      ret += 1;
    }
    ret
  }
}
