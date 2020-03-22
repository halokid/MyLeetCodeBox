package main

import (
  "testing"
)

type BubbleSorter interface {
  sort()
}

type Bubble struct {
  name      string
}

func TestEbullition(t *testing.T) {
  array := []int{4, 93, 22, 86, 57, 12, 29}
  bubble := Bubble{name: "冒泡---从小到大---稳定---n*n---"}
  bubble.sort(array)
  t.Log(array)
}

/**
主要 冒泡排序不是两两交换， 而是把循环对比， 把最轻的交换到应该在的位置
 */
func (b Bubble) sort(array []int) {
  for i := 0; i < len(array); i++ {
    for j := i + 1; j < len(array); j++ {
      if array[i] > array[j] {    // 最小的在左边
        array[i], array[j] = array[j], array[i]
      }
    }
  }
}

func (b Bubble) zSort(array []int) {
  for i := 0; i < len(array); i++ {
    for j := i + 1; j < len(array); j++ {
      if array[i] < array[j] {      // 最大的在左边
        array[i], array[j] = array[j], array[i]
      }
    }
  }
}

func bubbleSort(nums []int)  {
  for i := 0; i < len(nums); i++ {
    for j := 1; j < len(nums); j++ {
      if nums[j] < nums[j - 1] {
        // 交换
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
      }
    }
  }
}





