#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
def summary():
    with open('test_5.5.txt', 'w+') as f_sum:
        line = input('Введите цифры через пробел: \n')
        f_sum.writelines(line)
        my_numb = line.split()
        print("Сумма введеных чисел - ", sum(map(int, my_numb)))
summary()
