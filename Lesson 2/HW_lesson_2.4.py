#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
u_string = input("Введите слова через пробел: ")
u_word = []
start = 1
for i in range(u_string.count(' ') + 1):
    u_word = u_string.split()
    if len(u_word) <= 10:
        print(start, u_word[i])
        start += 1
    else:
        print(start, u_word[i[0:10]]) #не работает
        start += 1