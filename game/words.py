import random


# Загрузка слов и их инструкций из текстового файла
def load_words():
    words = {}
    with open("data/words.txt", encoding="utf-8") as f:
        for line in f:
            word, instruction = line.strip().split(':')
            words[word.strip()] = instruction.strip()
    return words


# Выбор случайного слова и его инструкции из словаря
def select_random_word(words):
    word = random.choice(list(words.keys()))
    instruction = words[word]
    return word, instruction