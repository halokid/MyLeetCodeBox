package main

import (
  "strings"
  "testing"
)

/**
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

 */

func reverseWords(s string) string {
  sx := ""
  sp := strings.Split(s, " ")
  for j, v := range sp {
    for i := len(v) - 1; i >= 0; i-- {
      sx += string(v[i])
    }
    if j != len(sp) - 1 {
      sx += " "
    }
  }
  return sx
}

func TestReverseWords(t *testing.T) {
  s := "Let's take LeetCode contest"
  t.Log(reverseWords(s))
}




