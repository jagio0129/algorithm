import random

for i in range(10):
  r = random.randint(1, 1000)
  print(r, "%s桁" % len(str(r)))