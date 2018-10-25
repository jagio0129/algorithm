def fibonacci(n):
  init = [1,1]
  for i in range(n):
    v = init[i] + init[i+1]
    if v >= n:
      return init
    init.append(v) 
    

### main
if __name__ == "__main__":
  N = 40
  ary = fibonacci(N)
  print(ary)