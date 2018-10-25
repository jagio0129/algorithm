import random

def gen_ary():
  ary = []
  for i in range(10):
    ary.append(random.randint(1,10))
  return ary

# お互いに共通する値を取得
def same_value(ary1, ary2):
  ary = []
  for v in ary1:
    if v in ary2:
      if not v in ary:
        ary.append(v)
  ary.sort()
  return ary

# 入っている値の羅列
def all_value(ary1, ary2):
  ary = []
  for v in ary1:
    if not v in ary:
      ary.append(v)
  for v in ary2:
    if not v in ary:
      ary.append(v)
  ary.sort()
  return ary

ary1 = gen_ary()
ary2 = gen_ary()
ary_same  = same_value(ary1,ary2)
ary_all   = all_value(ary1, ary2)

print("配列1：%s" % ary1)
print("配列2：%s" % ary2)
print("共通の数： %s" % ary_same)
print("どちらか入っている数： %s" % ary_all)
