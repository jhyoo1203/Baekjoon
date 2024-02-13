import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
word_dict = {}
num_list = []
value = 9
res = 0

for i in range(N):
    for j in range(len(words[i])):
        if words[i][j] in word_dict:
            word_dict[words[i][j]] += 10 ** (len(words[i]) - j - 1)
        else:
            word_dict[words[i][j]] = 10 ** (len(words[i]) - j - 1)

for word in word_dict.values():
    num_list.append(word)
num_list.sort(reverse=True)

for i in num_list:
    res += value * i
    value -= 1

print(res)