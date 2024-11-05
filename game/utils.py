# Проверка валидности ввода
def is_valid_letter(letter):
    valid_letters = 'йцукенгшщзхъфывапролджэячсмитьбюёәіңғүұқөһ'
    return len(letter) == 1 and letter.lower() in valid_letters


# Нормализация ввода
def normalize_input(letter):
    return letter.lower()