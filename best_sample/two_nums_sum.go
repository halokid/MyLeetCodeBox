package main
/**
两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标
 */
func twoSum(nums []int, target int) []int {
  d := make(map[int]int, len(nums))
  for i, v := range nums {
    if need, ok := d[target - v]; ok {
      return []int{i, need}
    }
   d[v] = i
  }

  return nil
}


