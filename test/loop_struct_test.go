/**
循环结构体的数组
 */
package main

import (
  "fmt"
  "testing"
)

type ListNodex struct {
  Val       int
  Next      *ListNodex
}

func TestLoopStruct(t *testing.T)  {
  c := ListNodex{3, nil}
  b := ListNodex{2, &c}
  a := ListNodex{1, &b}

  nodes := []ListNodex{a, b, c}
  for index, res := range nodes {
    fmt.Printf("%d--------%v\n", index, res)
  }
}
