# homework lesson: 3, task 6
"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


# Очень простая реализация
def int_func_1(text: str) -> str:
    """
    Функция принимает строку и переводит первую букву каждого слова в заглавную.
    :param text: str
    :return: str
    """
    if text.replace(' ', '').isalpha():  # проверка, что слово(слова) состоят из букв
        return text.title()
    else:
        return "В функцию передали не слово!"


# Реализация немного сложнее
def int_func_2(text: str) -> str:
    """
    Функция принимает строку и переводит первую букву каждого слова в заглавную.
    :param text: str
    :return: str
    """
    result = []
    if text.replace(' ', '').isalpha():  # проверка, что слово(слова) состоят из букв
        for word in text.split(' '):
            word_to_list = list(word)
            word_to_list[0] = word[0].upper()
            word = ''.join(word_to_list)
            result.append(word)
        return ' '.join(result)
    else:
        return "В функцию передали не слово!"


text_1 = 'book'
text_2 = 'the title of the book'
print(int_func_1(text_1))
print(int_func_2(text_1))
print(int_func_1(text_2))
print(int_func_2(text_2))
