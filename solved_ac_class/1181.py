import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(input().rstrip())

set_list = set(lst)
lst = list(set_list)
lst.sort()
lst.sort(key=len)

for word in lst:
    print(word)