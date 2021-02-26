string = input().split()
words = []
for s in string:
    if s.endswith("s"):
        words.append(s)
words = "_".join(words)
print(words)
