import random
from fractions import Fraction

# 帯分数化
# return t:整数部, numerator:分子, denominator:分母
def mixed_fractionize(numerator, denominator):
  # 分子を分母で割り切れるなら整数
  if numerator % denominator == 0:
    return str(int(numerator/denominator))

  # 分子が分母より大きいなら帯分数化
  if numerator > denominator:
    t = int(numerator / denominator)
    numerator = numerator - t*denominator
    return str(t) + "." + str(numerator) + "/" + str(denominator)

  # 帯分数化できないならそのまま
  return str(numerator) + "/" + str(denominator)

### main
if __name__ == '__main__':
  for i in range(10):
    numerator1    = random.randint(1, 10) # 分子
    denominator1  = random.randint(1, 10) # 分母
    fraction1     = Fraction(numerator1, denominator1)
    s1            = mixed_fractionize(numerator1, denominator1)

    numerator2    = random.randint(1, 10) # 分子
    denominator2  = random.randint(1, 10) # 分母
    fraction2     = Fraction(numerator2, denominator2)
    s2            = mixed_fractionize(numerator2, denominator2)

    sum = fraction1 + fraction2
    ss  = mixed_fractionize(sum.numerator, sum.denominator)

    print("%s + %s = %s" % (s1, s2, ss))