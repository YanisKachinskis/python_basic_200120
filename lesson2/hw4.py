user_string = input('Введите строку из нескольких слов:\n').split()

for i, j in enumerate(user_string, 1):
    print(i, j[:10])
