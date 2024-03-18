import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

cards = []

for card in a:
    heapq.heappush(cards, card)


for _ in range(m):
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    
    heapq.heappush(cards, card1 + card2)
    heapq.heappush(cards, card1 + card2)


print(sum(cards))