from game.ui import display_hangman, display_word_state, display_incorrect_guesses, display_instruction
from game.utils import is_valid_letter, normalize_input

# Класс игры
class Game:
    # Конструктор класса
    def __init__(self, word, instruction, max_attempts=6):
        self.word = word
        # Нормализация слова для упрощения сравнения
        self.normalized_word = self.word.lower()
        self.instruction = instruction
        # Максимальное количество попыток
        self.max_attempts = max_attempts
        self.guessed_letters = []
        self.incorrect_guesses = []
        self.remaining_attempts = max_attempts

    # Метод для ввода буквы
    def make_guess(self, letter):
        letter = normalize_input(letter)
        # Проверка валидности ввода
        if not is_valid_letter(letter):
            print("Invalid input. Please enter a valid letter.")
            return
        # Проверка на повторное введение буквы
        if letter in self.guessed_letters or letter in self.incorrect_guesses:
            print(f"You've already guessed '{letter}'. Try again.")
            return
        
        # Проверка наличия буквы в слове
        if letter in self.normalized_word:
            self.guessed_letters.append(letter)
        else:
            # Уменьшение количества попыток
            self.incorrect_guesses.append(letter)
            self.remaining_attempts -= 1


    # Метод для проверки выигрыша
    def is_game_won(self):
        return all(letter.lower() in self.guessed_letters for letter in self.word if letter != ' ')


    # Метод для проверки проигрыша
    def is_game_lost(self):
        return self.remaining_attempts == 0


    # Метод для отображения состояния игры
    def display_game_state(self):
        # Отображение инструкции для слова
        display_instruction(self.instruction)
        # Отображение виселицы
        display_hangman(self.remaining_attempts)
        # Отображение слова с угаданными буквами и подчеркиваниями для неугаданных букв
        display_word_state(self.word, self.guessed_letters)
        # Отображение неверно угаданных букв
        display_incorrect_guesses(self.incorrect_guesses)

    def play(self):
        print("Welcome to Hangman!")
        while not self.is_game_won() and not self.is_game_lost():
            self.display_game_state()
            guess = input("Enter a letter: ")
            self.make_guess(guess)

        if self.is_game_won():
            print(f"Congratulations! You've guessed the word: {self.word}")
        else:
            display_hangman(self.remaining_attempts)
            print(f"Game over! The word was: {self.word}")