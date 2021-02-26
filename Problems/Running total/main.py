string = input()

string_to_num = [int(x) for x in string]
string_sum = []
total = 0
for x in string_to_num:
    total += x
    string_sum.append(total)
print(string_sum)
