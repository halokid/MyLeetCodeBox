impl Solution {
  fn reverse_string(s: &mut Vec<char>) {
    let len = s.len();
    for i in 0..(len+1)/2 {
      let tmp = s[i];
      s[i] = s[len - 1 - i];
      s[len -1 - i] = tmp
    }
  }
}