#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

u_month = int(input("Введите месяц от 1 до 12: "))
#решение через List
month_list = ["зима", "весна", "лето", "осень"]
#Решение через dict
month_dict = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
if 1 <= u_month < 3 or u_month == 12:
    print(month_list[0])
    print(month_dict.get(1))
elif 3 <= u_month < 6:
    print(month_list[1])
    print(month_dict.get(2))
elif 6 <= u_month < 9:
    print(month_list[2])
    print(month_dict.get(3))
elif 9 <= u_month < 12:
    print(month_list[4])
    print(month_dict.get(4))
elif u_month > 12:
    print(u_month, "- и на такой месяц код сработает =)")
