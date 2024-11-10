import random

class RandomizedSet:

  def __init__(self):
    self.r_set = set()

  def insert(self, val: int) -> bool:
    if val in self.r_set:
      return False
    else:
      self.r_set.add(val)
      return True

  def remove(self, val: int) -> bool:
    if val not in self.r_set:
      return False
    self.r_set.remove(val)
    return True

  def getRandom(self) -> int:
    # return self.r_set.pop()
    random_element = random.choice(list(self.r_set))
    return random_element

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
  obj = RandomizedSet()
  p1 = obj.insert(1)
  print('p1 a -->>>', p1)
  p1 = obj.insert(1)
  print('p1 b -->>>', p1)

  p1 = obj.insert(3)
  p1 = obj.insert(4)

  p2 = obj.remove(2)
  print('p2 a -->>>', p2)
  p2 = obj.remove(3)
  print('p2 b -->>>', p2)

  obj.insert(12)
  obj.insert(9)
  obj.insert(7)
  print('obj -->>>', obj.r_set)
  p3 = obj.getRandom()
  print('p3 -->>>', p3)











