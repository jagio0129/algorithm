# 約数一覧を配列で返す
def divisor_list(n):
  ary = []
  for v in range(1,int(n/2)+1):
    if n % v == 0:
      ary.append(v)
  return ary

# 完全数を表示
def perfect_number(n):
  d_ary = divisor_list(n)

  # 約数を全て足し合わせる
  sum = 0
  for v in d_ary:
    sum += v
  
  # 完全数を表示
  if n == sum:
    print(n)

### main
if __name__ == '__main__':
  print("Show Perfect Number")

  N = 10000
  for i in range(1, N+1):
    perfect_number(i)
