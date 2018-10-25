def toribonacci(n):
  init = [1,1,2]
  for i in range(n):
    v = init[i] + init[i+1] + init[i+2]
    if v >= n:
      return init
    init.append(v) 
    

### main
if __name__ == "__main__":
  N = 30
  ary = toribonacci(N)
  print(ary)