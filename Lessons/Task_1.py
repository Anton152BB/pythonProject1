#Задание 1 - Запрос и вывод"Число четное"/"Число нечетное"
number = int(input('Введите число: '))
if number % 2 == 0: print('Четное число')
else:
    print('Нечетное число')

#Задание 2 - Программа, которая просит ввести свой возраст и выводит сообщение
age = int(input('Введите ваш возраст:'))
if age < 12:
    print("Детство")
elif 12 <= age <= 18:
    print("Подросток")
else:
    print("Взрослый")

#Задание 3 - While
a = 0
total = 0
while a <= 10:
	total += a
	a += 1
print(total)

#Задание 4
for a in range(1, 6):
    square = a ** 2
    print(f"Квадрат числа {a}: {square}")





