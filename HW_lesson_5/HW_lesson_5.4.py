#4. Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
import codecs
import os
dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with codecs.open('test_5.4.txt', 'r', 'utf_8_sig') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(dict[i[0]] + '  ' + i[1])

with codecs.open('test_5.4_trslt.txt', 'w', 'utf_8_sig') as file_obj_2:
    file_obj_2.writelines(new_file)
    print("Смотри test_5.4.trslt.txt")
os.system('explorer "test_5.4_trslt.txt"') #открывает файл в винде.