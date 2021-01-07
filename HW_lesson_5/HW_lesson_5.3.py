#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
import codecs
with codecs.open('test_5.3.txt', 'r', 'utf_8_sig') as workers:
    sal = []
    poor = []
    sum_list = workers.read().split('\n')
    for i in sum_list:
        i = i.split()
        if float(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, sal)) / len(sal)}')