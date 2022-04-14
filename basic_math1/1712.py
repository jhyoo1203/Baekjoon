A, B, C = map(int, input().split())
# A : 고정비용, B : 가변 비용, C : 판매비용
# C * n > A + (B * n) 일 때 손익분기점

if B >= C:
    print(-1)
else:
    print(int(A/(C-B) + 1))