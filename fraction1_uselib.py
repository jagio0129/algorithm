import random
from fractions import Fraction

# 帯分数化
def mixed_fractionize(fraction):
  numerator, denominator = fraction.numerator, fraction.denominator 

  # 整数ならそのまま返す
  if numerator % denominator == 0:
    return str(fraction)

  # 分子の方が大きければ帯分数化
  if numerator > denominator:
    i = int(numerator / denominator)
    numerator = numerator - denominator*i
    return str(i) + "." + str(numerator) + "/" + str(denominator)

  # 分子の方が小さければそのまま返す。
  return str(fraction)

if __name__ == "__main__":
  # 10回ループ
  for i in range(0,10):
    numerator1    = random.randint(1, 10) # 分子
    denominator1  = random.randint(2, 10) # 分母
    fraction1     = Fraction(numerator1, denominator1)
    s1 = mixed_fractionize(fraction1)
    
    numerator2   = random.randint(1, 10) # 分子
    denominator2 = random.randint(2, 10) # 分母
    fraction2     = Fraction(numerator2, denominator2)
    s2 = mixed_fractionize(fraction2)

    sum = fraction1 + fraction2
    ss = mixed_fractionize(sum)

    print("%s + %s = %s" % (s1, s2, ss))