X = int(input())
num = 0
count = 1
 
while X > num:
  num += count
  count += 1

line = X - (num - (count - 1))

if count % 2 == 0:
  print(f"{count-line}/{line}")
else:
  print(f"{line}/{count-line}")