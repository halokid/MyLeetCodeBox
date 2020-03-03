package main

import (
  "fmt"
  "testing"
)

func singleNumber(nums []int) int {
  tmp := make(map[int]int)
  tmpI := 0
  for _, i := range nums {
    if _, ok := tmp[i]; ok {
      delete(tmp, i)
    } else {
      tmp[i] = 0
      tmpI = i
    }
    fmt.Println(tmp)
  }

  for k, _ := range tmp {
    //fmt.Println(k, v)
    tmpI = k
  }
  return tmpI
}

func singleNumer2(nums []int) int {
  xOrA := 0
  for _, i := range nums {
    xOrA ^= i
  }
  return xOrA
}

func TestNumAppearOnce(t *testing.T) {
  nums := []int{4, 1, 2, 1, 2}
  i := singleNumber(nums)
  t.Log(i)

  j := singleNumer2(nums)
  t.Log(j)
}



