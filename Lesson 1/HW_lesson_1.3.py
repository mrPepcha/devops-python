#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
n = (input("Введите число - "))
a = (n+n)
b = (n+n+n)
total = int(n) + int(a) + int(b)
print(f"Сумма чисел n + nn + nnn - {total}  ")