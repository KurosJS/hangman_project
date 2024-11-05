# Интерфейс пользователя
def display_hangman(attempts_left):
    stages = [
        """
           ------
           |    |
           O    |
          /|\   |
          / \   |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
          /|\   |
          /     |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
          /|\   |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        =========
        """,
        """
           ------
           |    |
                |
                |
                |
                |
        =========
        """
    ]
    print(stages[attempts_left])


# Отображение слова с угаданными буквами и подчеркиваниями для неугаданных букв
def display_word_state(word, guessed_letters):
    display = ''
    for letter in word:
        if letter == ' ':
            display += ' '  # Leave spaces as they are
        elif letter.lower() in guessed_letters:
            display += letter  # Show the letter in its original case
        else:
            display += '_'  # Display underscores for unguessed letters
    print(f"Word: {display}")


# Отображение неверно угаданных букв
def display_incorrect_guesses(incorrect_letters):
    print(f"Incorrect guesses: {', '.join(incorrect_letters)}")


# Отображение инструкции для слова
def display_instruction(instruction):
    print(f"Hint: {instruction}")