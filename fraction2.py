import random
from fractions import Fraction

for i in range(10):
  numerator1    = random.randint(1, 10) # 分子
  denominator1  = random.randint(1, 10) # 分母
  fraction1     = Fraction(numerator1, denominator1)

  numerator2   = random.randint(1, 10) # 分子
  denominator2 = random.randint(1, 10) # 分母
  fraction2     = Fraction(numerator2, denominator2)