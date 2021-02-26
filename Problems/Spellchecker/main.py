dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
sentence = input().split()
incorrect = []
for word in sentence:
    if word not in dictionary:
        incorrect.append(word)
if len(incorrect) == 0:
    print("OK")
else:
    for word in incorrect:
        print(word)
