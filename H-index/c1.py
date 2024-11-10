import math
from typing import List

DEBUG = True


def debug(*s):
  if DEBUG:
    print(*s)


def checkIndex(citations, middle) -> bool:
  check = 0
  for i in citations:
    if i >= middle:
      check += 1

  debug("----------------------")
  debug('check: ', check, ', middle:', middle)

  # return check == middle
  return check >= middle


class Solution:
  def hIndex(self, citations: List[int]) -> int:
    # middle = math.ceil(len(citations) / 2)
    middle = math.ceil(sum(citations) / 2)

    middle = min(len(citations), middle)

    while middle > 0:
      if not checkIndex(citations, middle):
        middle -= 1
      else:
        return middle
    return 0


if __name__ == "__main__":
  # citations = [3, 0, 6, 1, 5]
  # citations = [1, 3, 1]
  # citations = [1, 6, 1]
  # citations = [1, 6, 1, 2]
  # citations = [0]
  # citations = [0, 0]
  # citations = [0, 0, 1]
  # citations = [0, 0, 0]
  citations = [11, 15]
  solu = Solution()
  index = solu.hIndex(citations)
  print('index 1 -->>>', index)
