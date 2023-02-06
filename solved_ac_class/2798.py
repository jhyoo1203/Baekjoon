import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
res = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if nums[i] + nums[j] + nums[k] > m:
                continue
            else:
                res = max(res, nums[i]+nums[j]+nums[k])

print(res)