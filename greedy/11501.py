import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.reverse()
    max = nums[0]
    res = 0

    for i in range(1, N):
        if max < nums[i]:
            max = nums[i]
            continue
        res += max - nums[i]
    
    print(res)