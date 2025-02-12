import random, string

def generate_random_string(length):
    """Генерация случайной строки
    в аргументе - длина генерируемой строки"""
    # Символы для генерации случайной строки: буквы и цифры
    characters = string.ascii_letters + string.digits
    # Генерация случайной строки заданной длины
    return ''.join(random.choices(characters, k=length))