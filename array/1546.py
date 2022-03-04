n = int(input())
test_list = list(map(int, input().split()))
max_score = max(test_list)

new_list = []
for score in test_list:
  new_list.append(score/max_score*100)

result = sum(new_list)/n
print(result)