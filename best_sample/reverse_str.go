package main
/**
记住一个原则， string转化为byte肯定性能更好
 */
import "bytes"

func reverseWords(s string) string {
  wordsByte := bytes.Split([]byte(s), []byte{' '})
  for i, word := range wordsByte {
    for j := 0; j < len(word) / 2; j++ {
      word[j], word[len(word) - 1 - j] = word[len(word) - 1 - j], word[j]
    }
    wordsByte[i] = word
  }
  return string(bytes.Join(wordsByte, []byte{' '}))
}
