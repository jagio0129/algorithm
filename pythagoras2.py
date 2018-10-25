
N = 100

# a, bの重複を許さない
for a in range(1, N+1):
  for b in range(a, N+1):
    for c in range(1, N+1):
      if a*a + b*b == c*c:
        print("a:%s, b:%s, c:%s" % (a,b,c))