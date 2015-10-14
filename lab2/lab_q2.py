add = 0
num = 1
lastnum = 0
nextnum = 0
while nextnum < 4000000:
  nextnum = num + nextnum
  num = nextnum - num
  if num % 2 == 0:
    add = add + num
print add