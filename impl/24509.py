import sys, heapq
input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
korean, english, math, science = [], [], [], []
award = set()

for i in range(N):
    korean_score, english_score, math_score, science_score = data[i][1], data[i][2], data[i][3], data[i][4]
    heapq.heappush(korean, (-korean_score, data[i][0]))
    heapq.heappush(english, (-english_score, data[i][0]))
    heapq.heappush(math, (-math_score, data[i][0]))
    heapq.heappush(science, (-science_score, data[i][0]))

for subject_heap in [korean, english, math, science]:
    while True:
        _, student = heapq.heappop(subject_heap)
        if student not in award:
            award.add(student)
            print(student, end=' ')
            break