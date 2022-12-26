import sys
input = sys.stdin.readline

n = input()
n_list = list(n.rstrip())
n_list.sort(reverse=True)
result = 0

for num in n_list:
    result += int(num)
if '0' not in n_list or result % 3 != 0:
    print(-1)
else:
    print(''.join(n_list))
