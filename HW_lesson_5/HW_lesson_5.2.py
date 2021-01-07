#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open("test_5.2.txt", 'r') as file_obj:
    file_obj.readline()
with open("test_5.2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} - количество слов в строке")
    print(f"Количество строк - {lines}")