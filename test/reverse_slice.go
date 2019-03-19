package main

import (
  "fmt"
)

func main() {
  fmt.Println(reverse1([]byte{11,22,33,44}))

  fmt.Println(reverse2([]int{11, 22, 33, 44}))
}


func reverse1(s []byte) []byte {
  for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
    s[i], s[j] = s[j], s[i]
  }
  return s
}

func reverse2(s []int) []int {
  for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
    s[i], s[j] = s[j], s[i]
  }
  return s
}

