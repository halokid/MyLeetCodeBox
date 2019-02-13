package main

import "fmt"

func twoSums(nums []int, target int) []int {
  for i := 0; i < len(nums); i++ {
    for j := i+1; j < len(nums); j++ {
      if nums[i] + nums[j] == target {
        return []int{i, j}
      }
    }
  }
  return []int{}
}

func main() {
  nums := []int{2, 7, 11, 15}
  target := 22
  twoNums := twoSums(nums, target)
  fmt.Println(twoNums)
}
