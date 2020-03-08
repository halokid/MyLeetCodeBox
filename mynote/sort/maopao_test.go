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

func (b Bubble) sort(array []int) {
  for i := 0; i < len(array); i++ {
    for j := i + 1; j < len(array); j++ {
      if array[i] > array[j] {
        array[i], array[j] = array[j], array[i]
      }
    }
  }

}
