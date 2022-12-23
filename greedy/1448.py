import sys
input = sys.stdin.readline

n = int(input())
list = []
for _ in range(n):
    r = int(input())
    list.append(r)
list.sort(reverse=True)
bool = False

for i in range(len(list)-2):
    if list[i] < list[i+1] + list[i+2]:
        print(list[i] + list[i+1] + list[i+2])
        bool = True
        break
if bool == False:
    print(-1)
