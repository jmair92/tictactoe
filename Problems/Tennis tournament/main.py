n = int(input())
names = []
for _ in range(n):
    name = input().split(" ")
    if name[1] == "win":
        names.append(name[0])
number_of_wins = len(names)
print(names)
print(number_of_wins)
