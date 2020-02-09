package main

import (
  "github.com/spf13/cast"
  "log"
  "os"
)

var in int

func odd(num int) int {
  if num % 2 == 0 || num == 1 {
    return num
  }
  in += 1
  log.Print("num --------", num - 1)
  return num - 1
}

func even(num int) int {
  if num % 2 != 0 || num == 1 {
    return num
  }
  in += 1
  log.Print("num --------", num / 2)
  return num / 2
}

func numberOfSteps(num int) int {
  //log.Print("num start ------------", num)
  //return 0
  in := 0
  for {
    if num == 0 {
     return in
    }
    if num % 2 == 0 {
      num = num / 2
      in += 1
      log.Print("num ------------", num)
    }
    if num % 2 != 0 {
      num = num - 1
      in += 1
      log.Print("num ------------", num)
    }
  }
  //return in
}

var xn int = 0
func numberOfSteps2(num int) int {
  // 递归方式
  //in := 0
  if num == 0 {
    return 1
  }
  if num % 2 == 0 {
    num = num / 2
  } else {
    num = num -1
  }
  xn = 1
  xn += numberOfSteps2(num)
  return xn
}

func main() {
  args := os.Args
  log.Print(args)
  num := cast.ToInt(args[1])
  /**
  for {
    if num == 1 {
      break
    }
    num = odd(num)
    num = even(num)
  }
  log.Print("步骤数为 ------------", in+1)
  */
  log.Print("+++++++++++++++++++++++++++++++++++++++")
  //log.Print(numberOfSteps(num))
  log.Print(numberOfSteps2(num))
}



