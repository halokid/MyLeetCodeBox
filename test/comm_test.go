package main

import (
  "github.com/spf13/cast"
  "testing"
)

func TestC1(t *testing.T) {
  s := "hello"
  t.Log(cast.ToString(s[1]))    // output ASCII format

  const sample = "\xbd\xb2\xbc\x20\x8c\x98"
  t.Logf("%x", sample)

  for i := 0; i < len(sample); i++ {
    t.Logf("%x", sample[i])
  }

  t.Logf("%q", sample)

  t.Log(string([]rune(s)[3]))
  t.Log(string(s[3]))
  t.Log(len(s))
}


