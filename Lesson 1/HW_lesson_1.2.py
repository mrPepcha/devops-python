#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
u_sec = int(input("Введите секунды >>> "))
hours = u_sec // 3600
minutes = (u_sec - hours * 3600) // 60
seconds = u_sec - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {u_sec} : {minutes} : {seconds}")
