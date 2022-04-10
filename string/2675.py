T = int(input())

for i in range(T):
  R, S = input().split()
  R = int(R)
  for word in S:
    for _ in range(R):
      print(word, end='')
  print()
