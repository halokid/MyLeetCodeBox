# coding=utf-8

string = 'abc123456'
i=3
j=5
print(string)
temp = string[j]
# 先取出来 j 后面的那段字符
trailer = string[j+1:] if j + 1 < len(string) else ''

# 先改第一个字符, 改成要替换的那个
string = string[0:j] + string[i] + trailer
# 再改第二个字符， 改成要替换的那个
string = string[0:i] + temp + string[i+1:]
print(string)


