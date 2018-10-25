import random
from fractions import Fraction

# Fractionライブラリを使う場合
def use_fraction():
  numerator1    = random.randint(1, 10) # 分子
  denominator1  = random.randint(2, 10) # 分母
  fraction1     = Fraction(numerator1, denominator1)

  numerator2   = random.randint(1, 10) # 分子
  denominator2 = random.randint(2, 10) # 分母
  fraction2     = Fraction(numerator2, denominator2)

  sum = fraction1 + fraction2
  if sum > 1:
    v = int(sum.numerator / sum.denominator)
    n_sum = sum - v
    if n_sum.numerator == 0:
      print("%s + %s = %s" % (fraction1, fraction2, v))
    else:
      sum = str(v) + "." + str(n_sum)
      print("%s + %s = %s" % (fraction1, fraction2, sum))
      
# Fractionを使わずに自前で実装
class FullScratch:

  # コンストラクタ
  # def __init__(self):
    
  # 最小公倍数の算出
  def least_common_multiple(self, a, b):
    return int(a*b / self.greatest_common_divisor(a,b))

  # 最大公約数
  def greatest_common_divisor(self, a, b):
    # 大きい方がaとなるようにする
    if a < b:
      tmp = a
      a = b
      b = tmp

    # ユークリッド互除法
    r = a % b
    while(r != 0):
      a = b
      b = r
      r = a % b
    return b

  # 約分した分子・分母を返す
  def reduction(self, numerator, denominator):
    lcm = self.greatest_common_divisor(numerator, denominator)
    
    n = int(numerator / lcm)
    d = int(denominator / lcm)
    return n, d

  # 帯分数化
  # return t:整数部, numerator:分子, denominator:分母
  def mixed_fractionize(self, numerator, denominator):
    t = None
    if numerator >= denominator:
      t = int(numerator / denominator)
      numerator = numerator - t*denominator
    return t, numerator, denominator

  # 分数を最適化
  def optimize(self, numerator, denominator):
    # 約分
    numerator, denominator = self.reduction(numerator, denominator)
    # 帯分数化
    t, numerator, denominator = self.mixed_fractionize(numerator, denominator)
    return t, numerator, denominator

  # 分数形式の文字列する
  def fraction_str(self, t, numerator, denominator):
    # 整数化
    if numerator == 0:
      return str("%s" % t)
    # 分数化
    if t is None:
      return str("%s/%s" % (numerator, denominator))
    # 帯分数化
    else:
      return str("%s.%s/%s" % (t, numerator, denominator))

# 自前実装
def full_scratch():
  fc = FullScratch()

  # １項
  numerator1    = random.randint(1, 10) # 分子
  denominator1  = random.randint(2, 10) # 分母
  t1, n1, d1 = fc.optimize(numerator1, denominator1) # 最適化
  s1 = fc.fraction_str(t1,n1,d1)

  # ２項
  numerator2    = random.randint(1, 10) # 分子
  denominator2  = random.randint(2, 10) # 分母
  t2, n2, d2 = fc.optimize(numerator2, denominator2) # 最適化
  s2 = fc.fraction_str(t2,n2,d2)

  # 計算
  ans_num = numerator1*denominator2 + numerator2*denominator1 # 分子
  ans_den = denominator1*denominator2                         # 分母
  ta, na, da = fc.optimize(ans_num, ans_den)
  sa = fc.fraction_str(ta,na,da)

  # 式の出力
  print("%s + %s = %s" % (s1, s2, sa))

### main
if __name__ == '__main__':
  # 10回ループ
  for i in range(0,10):
    # 自前の処理
    # full_scratch()
    # Fractionライブラリを使用
    use_fraction()