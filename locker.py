N = 50

# ロッカーの生成。デフォルトは-1(閉じている)
lockers = [-1 for i in range(N)]

for i in range(N):
  print("%s人目" % str(i+1))
  for j in range(len(lockers)):
    # 約数だったら
    if int((j+1)%(i+1)) == 0:
      # 扉の開け閉め
      if    lockers[j] == 1:
        lockers[j] = -1
      elif  lockers[j] == -1:
        lockers[j] = 1
print(lockers.count(1))    