package main

import "fmt"

func main() {
  x := 15
  y := x / 10     // 默认为int类型， 所以是1
  z := x % 10

  fmt.Println(y)
  fmt.Println(z)
}
