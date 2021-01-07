#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
test_list = []
while True:
    line = input("Введите слово: ")
    if line == '':
        print(test_list)
        exit()
    else:
        newline = line + '\n'
        test_list.append(newline)

    with open("test_5.1.txt", "w") as file_obj:
        file_obj.writelines(test_list)