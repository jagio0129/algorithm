import math

# 2〜nまでの自然数の配列を生成
def gen_ary(n):
  ary = []
  for i in range(2,n+1):
    ary.append(i)
  return ary

# 素数かどうか
def is_prime_number(n):
  for i in range(2,n):
    if n % i == 0:
      return False
  return True

# エラトステネス
def eratosthenes(ary):
  max = int(math.sqrt(ary[-1]) + 1)
  for i in range(0, max):
    v = ary[i]
    for j in range(2, len(ary)):
      if j > ary[-1]:
        break
      # vの倍数を削除
      if v*j in ary:
        ary.remove(v*j)
  return ary
      
### main
if __name__ == "__main__":
  N = 10000

  ary = gen_ary(N)
  ary = eratosthenes(ary)
  print(ary)