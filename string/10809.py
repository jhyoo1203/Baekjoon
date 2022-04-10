word = input()
alphabet = list(range(97,123))

for alpha in alphabet:
  print(f"{word.find(chr(alpha))} ", end='')