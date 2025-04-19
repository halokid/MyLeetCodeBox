from typing import List

DEBUG = True

def debug(*s):
  if DEBUG:
    print(*s)


ori_path = "root:root/aaa:aaa/bbb:bbb/ccc:ccc/ddd:ccc/eee:bbb:fff"

ori_path_sl = ori_path.split(':')
print('ori_path_sl -->>>', ori_path_sl)

def get_full_path(sub, ori_path_sl, get_path):
  print('------------------ sub -->>>', sub, '-------------------')
  if 'root/' in sub:
    print('-->>> should end!!!')
    return sub

  s = ''

  ck = sub
  sub_sl = sub.split('/')
  print('sub_sl -->>>', sub_sl)
  if len(sub_sl) > 0:
    ck = sub_sl[0]
  print('ck -->>>', ck)

  for item in ori_path_sl:
    print('item -->>>', item)
    if ck in item:
      # s = s + get_full_path(item, ori_path_sl)
      # s = s + ":" + item
      # set_path = s + ":" + get_full_path(item, ori_path_sl)
      # print('set_path -->>>', set_path)
      # return set_path

      print('fix item -->>>', item)
      # get_path += item
      s += item
      return s + ":" + get_full_path(item, ori_path_sl, get_path)
  return s

if __name__ == "__main__":
  # get_full_path('ddd', ori_path_sl)
  get_path = "x"
  real_path = get_full_path('ccc/ddd', ori_path_sl, get_path)
  print('real_path -->>>', real_path)
  print(get_path)

  # real_path -->>> bbb/ccc:aaa/bbb:root/aaa:root/aaa
  real_path_sl = real_path.split(":")
  real_path_sl.reverse()
  print('real_path_sl -->>>', real_path_sl)
  fix_path = ""
  i = 0
  for item in real_path_sl[1:]:
    if i == 0:
      fix_path += item + "/"
    else:
      item_sl = item.split("/")
      fix_path += item_sl[1] + "/"
    i += 1

  print('fix_path -->>>', fix_path)


