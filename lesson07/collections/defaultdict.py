import collections

d = collections.defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(3)

print(d)

d = collections.defaultdict(int)

# Збільшення значення для кожного ключа
d['a'] += 1
d['b'] += 1
d['a'] += 1

print(d)

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}

for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)

print(grouped_words)

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = collections.defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(dict(grouped_words))