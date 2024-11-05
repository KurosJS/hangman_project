from game.game import Game
from game.words import load_words, select_random_word


if __name__ == "__main__":
    # Загрузка слов и их инструкций из текстового файла
    words = load_words()
    random_word, instruction = select_random_word(words)
    
    # Создание экземпляра игры и запуск игры
    game = Game(random_word, instruction)
    game.play()