import random

# 配列を降順に並び替える
def dec_sort(ary):
  for n in range(len(ary)):
    # 最大値を探す
    maxi, max = 0, 0
    for i, v in enumerate(ary[n:]):
      if v > max:
        maxi, max = i+n, v
    # 最大値項とi項を入れ替える
    tmp = ary[n]
    ary[n] = ary[maxi]
    ary[maxi] = tmp
    print(ary)
  return ary

data = [random.randint(1, 100) for i in range(10)]
sorted_ary = dec_sort(data)
print(data)
print(sorted_ary)