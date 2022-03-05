c = int(input())
for i in range(c):
  score_list = list(map(int, input().split()))
  avg = sum(score_list[1:]) / score_list[0]
  count = 0
  for j in range(1, len(score_list)):
    if score_list[j] > avg:
      count += 1
  result = count / score_list[0] * 100
  print(f'{result:.3f}%')