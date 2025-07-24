import string
print("Введите текст (пустая строка — завершение ввода):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = "\n".join(lines)
text_lower = text.lower()

punct = string.punctuation + "—…«»„“”№–"
clean_text = ''.join([char if char.isalnum() or char.isspace() else ' ' for char in text_lower])
words = clean_text.split()
unique_words = set(words)
unique_word_count = len(unique_words)

longest_word = max(words, key=len) if words else ""

from collections import Counter
letters_only = [char for char in text_lower if char.isalpha()]
letter_freq = Counter(letters_only)
sorted_freq = dict(sorted(letter_freq.items()))

print("\nСтатистика по тексту:")
print(f"Уникальных слов: {unique_word_count}")
print(f"Самое длинное слово: {longest_word}")
print("Частота букв:")
for letter, count in sorted_freq.items():
    print(f"{letter}: {count}")