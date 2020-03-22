package main

import (
  "math/rand"
  "testing"
  "time"
)

func initData(arr []int) {
  for i, _ := range arr {
    arr[i] = rand.Intn(100)
  }
}

func QuickSort(arr []int, idxStart int, idxEnd int) {
  // 递归函数出口
  if idxStart >= idxEnd {
    return
  }

  // 基准数
  num := arr[idxStart]
  i := idxStart
  j := idxEnd

  // 找到num合适的位置
  for {
    if i >= j {
      break
    }

    // 将比基准数小的放到它的左边
    for {
      if i >= j {
        break
      }
      if arr[j] < num {
        arr[i] = arr[j]
        i++       // i 往前移动
        break
      }
      j--
    }  // END for 1

    // 将比基准大的放到它的右边
    for {
      if i >= j {
        break
      }
      if arr[i] >= num {
        arr[j] = arr[i]
        j--       // j 往后移动
        break
      }
      i++
    }

  }   // END for all

  // 将基准数放到 它 应该有的位置
  arr[i] = num
  // 将左边 进行同样的排序
  QuickSort(arr, idxStart, i)
  // 将右边 进行同样的排序
  QuickSort(arr, i + 1, idxEnd)
}

func TestQuickSort(t *testing.T) {
  rand.Seed(time.Now().UnixNano())

  n := 10
  arr := make([]int, n, n)

  // init data
  initData(arr)
  t.Log(arr)
  // quick sort
  QuickSort(arr, 0, len(arr) - 1)
  t.Log(arr)
}










