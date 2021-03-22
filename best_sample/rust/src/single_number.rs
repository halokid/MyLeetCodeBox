
impl Solution {
  pub fn single_number(nums: Vec<i32>) -> i32 {
    let mut acc = nums[0];
    let length = nums.len();
    for i in 0..length-1 {
      acc = acc ^ nums[i+1]
    }
    return acc;
  }
}