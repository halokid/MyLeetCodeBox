/**
两数之和
 */
package main

import "fmt"

// 暴力解法
func twoSum1(nums []int, target int) []int {
  for i := 0; i < len(nums); i++ {
    for j := i+1; j < len(nums); j++ {
      if nums[j] == target - nums[i] {
        return []int{i, j}
      }
    }
  }
  return []int{}
}

// 两遍哈希表, 原理就是 空间换时间
func twoSum2(nums []int, target int) []int {
  hashMap := make(map[int]int)
  // 第一遍
  // 先把list储存进map, 作为map的key
  for i := 0; i < len(nums); i++ {
    hashMap[nums[i]] = i
  }

  // 第二遍
  for i := 0; i < len(nums); i++ {
    complement := target - nums[i]
    // 判断是否含有complement这个key
    //if _, ok := hashMap[complement]; ok && hashMap[complement] != i {
    if _, ok := hashMap[complement]; ok {
      return []int{i, hashMap[complement]}
    }
  }
  return []int{}
}

func main() {
  nums := []int{2, 7, 11, 15}
  target := 13
  fmt.Println(twoSum1(nums, target))
  fmt.Println(twoSum2(nums, target))
}



