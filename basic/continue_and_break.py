a = True
while a:
  b = input('type something ')
  if b == '1':
    a = False
  else:
    pass

# break continue
for num in range(10):
  if num == 2:
    continue
  print(num)
  if num == 9:
    break