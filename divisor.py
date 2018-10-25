import random

i = random.randint(1, 1000)
print("Number: %s" % i)

for v in range(1, i, 1):
  if i % v == 0:
    print(v)