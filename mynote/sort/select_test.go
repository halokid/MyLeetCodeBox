package main

import "testing"

type SortInterface interface {
  sort()
}

type Sortor struct {
  name string
}

func TestSelect(t *testing.T) {
  array := []int{6, 1, 3, 5, 8, 4, 2, 0, 9, 7}
  learnsort := Sortor{name: "选择排序---从小到大---不稳定---n*n---"}
  learnsort.sort(array)

  t.Log(learnsort.name, array)
}

func (s Sortor) sort(array []int) {
  arrLen := len(array)
  for i := 0; i < arrLen; i++ {
    min := i
    for j := i + 1; j < arrLen; j++ {
      if array[j] < array[min] {
        min = j
      }
    }
    tmp := array[i]
    array[i] = array[min]
    array[min] = tmp
  }
}



