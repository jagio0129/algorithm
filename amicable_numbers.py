import random

# 約数の一覧を求める
def divisor(n):
  if not isinstance(n,int) or n < 0:
    raise
  if n == 1:
    return [1]
  return [i for i in range(1, int((n/2)+1)) if n % i == 0]
  
# 約数の総和を出す
def sum_divisor(n):
  ary = divisor(n)

  sum = 0
  for v in ary:
    sum += v
  return sum

# 友愛数であればその組み合わせを返す
def amicable_numbers(n):
  sum = sum_divisor(n)
  if n == sum_divisor(sum) and n != sum:
    return n, sum
  return None, None

### main
if __name__ == "__main__":
  N = 10000

  am_ary = []
  for i in range(1, N):
    # print("%s: %s, %s" % (i, divisor(i), sum_divisor(i)))
    num1, num2 = amicable_numbers(i)
    if not num1 is None:
      if not [num2, num1] in am_ary:
       am_ary.append([num1, num2])
      
  print(am_ary)