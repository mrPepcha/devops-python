#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
print("Текущий рейтинг: ", my_list)
u_digit = int(input("Введите вашу цифру: "))
for i in range(len(my_list)):
    if my_list[i] == u_digit:
        my_list.insert(i+1, u_digit)
        break
    elif my_list[0] < u_digit:
        my_list.insert(0, u_digit)
    elif my_list[-1] > u_digit:
        my_list.append(u_digit)
    elif my_list[i] > u_digit and my_list[i + 1] < u_digit:
        my_list.insert(i + 1, u_digit)
        break
print("Текущий список - ", my_list)

