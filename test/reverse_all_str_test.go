package main

import (
  "testing"
)

func reverseString(s []byte) string {
  left, right := 0, len(s) - 1
  for {
    if left >= right {
      break
    }
    s[left], s[right] = s[right], s[left]
    left, right = left + 1, right - 1
  }
  //fmt.Println(string(s))
  return string(s)
}

func TestReverseString(t *testing.T) {
  s := "hello"
  t.Log(s)
  t.Log(s[1])
  t.Log(string(s[1]))
  //t.Log([]byte(s[1]))

  sx := reverseString([]byte(s))
  t.Log(sx)

  sb := []byte(s)
  t.Log(sb[1])
  t.Log(string(sb[1]))
}
