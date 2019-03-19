/**
两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
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

// 一遍哈希表
func twoSum3(nums []int, target int) []int {
  hashMap := make(map[int]int)
  for i := 0; i < len(nums); i++ {
    complement := target - nums[i]

    if _, ok := hashMap[complement]; ok {
      return []int{i, hashMap[complement]}
    }

    hashMap[nums[i]] = i
  }
  return []int{}
}

func main() {
  nums := []int{2, 7, 11, 15}
  target := 13
  fmt.Println(twoSum1(nums, target))
  fmt.Println(twoSum2(nums, target))
  fmt.Println(twoSum3(nums, target))
}



