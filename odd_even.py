import random

ary = []
for i in range(10):
  ary.append(random.randint(1,100))

odd_ary, even_ary = [],[]
for v in ary:
  if v % 2 == 0:
    even_ary.append(v)
  else:
    odd_ary.append(v)
print(ary)
print("偶数：%s" % even_ary)
print("奇数：%s" % odd_ary)
