import random
import math

# エラトステネスの篩
def eratosthenes(n):
  if not isinstance(n, int):
    raise TypeError('n is int type.')
  if n < 2:
    raise ValueError('n is more than 2')

  prime = []
  limit = math.sqrt(n)
  # 2~nまでの配列を生成
  data = [i + 1 for i in range(1, n)]
  
  while True:
    p = data[0]
    if limit <= p:
      return prime + data
    prime.append(p)
    data = [e for e in data if e % p != 0]

# 素因数分解
def factoring(n):
  prime_ary = eratosthenes(n)
  data = []
  while True:
    for p in prime_ary:
      if n % p == 0:
        n = int(n / p)
        if n == 1:
          data.append(p)
          return data
        data.append(p)
        break

### main
if __name__ == '__main__':
  for i in range(10):
    n = random.randint(2,100)
    data = factoring(n)

    s = " × ".join(map(str, data))
    print("%s = %s" % (n, s))
