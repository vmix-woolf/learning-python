import collections

# task 01 - traditional way
student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1

print(mark_counts)

# the same with the Counter
student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
print(mark_counts)

print(mark_counts.most_common())
print(mark_counts.most_common(1))
print(mark_counts.most_common(2))

# Створення Counter з рядка
letter_count = collections.Counter("banana")
print(letter_count)
print(letter_count.most_common(1))

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = collections.Counter(words)
# Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")
