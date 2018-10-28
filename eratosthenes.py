import math

# エラトステネス
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
      print(prime)
      print(data)
      return prime + data
    prime.append(p)
    data = [e for e in data if e % p != 0]
      
### main
if __name__ == "__main__":
  N = 100

  data = eratosthenes(N)
  print(data)