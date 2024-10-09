int_var = 10
float_var = 3.14
str_var = "Привіт"
bool_var = True

print("Значення змінних:")
print("int_var:", int_var, "Тип:", type(int_var))
print("float_var:", float_var, "Тип:", type(float_var))
print("str_var:", str_var, "Тип:", type(str_var))
print("bool_var:", bool_var, "Тип:", type(bool_var))

a = 5
b = 2
c = 3

print("\nАрифметичні операції:")
print("Додавання:", a + b)
print("Віднімання:", a - b)
print("Множення:", a * b)
print("Ділення:", a / b)
print("Піднесення до степеня:", a ** b)

print("\nВикористання функцій:")
print("Округлення:", round(3.14159, 2))
print("Модуль числа:", abs(-7))
print("Остача від ділення:", a % b)

average = (a + b + c) / 3
print("Середнє арифметичне чисел 5, 2, 3:", average)

name = "Олексій"
age = 25

print("\nРобота з рядками:")
print("Конкатенація:", name + " " + str(age))
print("Зміна регістру:", name.upper())
print(f"Мене звати {name} і мені {age} років.")  

user_input = int(input("\nВведіть число для перевірки на парність: "))
if user_input % 2 == 0:
    print(f"Число {user_input} є парним.")
else:
    print(f"Число {user_input} є непарним.")

if 10 <= user_input <= 50:
    print(f"Число {user_input} входить в діапазон від 10 до 50.")
else:
    print(f"Число {user_input} не входить в діапазон від 10 до 50.")

print("\nЦикл for:")
for i in range(1, 11):
    print(i)

sum_value = 0
n = 1
while n <= 100:
    sum_value += n
    n += 1
print(f"\nСума чисел від 1 до 100: {sum_value}")

def add_two_numbers(x, y):
    return x + y

def reverse_string(s):
    return s[::-1]

print("\nФункції:")
print("Сума чисел 5 і 7:", add_two_numbers(5, 7))
print("Рядок у зворотному порядку:", reverse_string("Привіт"))

numbers = [10, 20, 30, 40, 50]

print("\nСписок:")
for number in numbers:
    print(number)

numbers.append(60)
print("\nСписок після додавання елементу:", numbers)

numbers.pop()
print("Список після видалення останнього елементу:", numbers)

student = {
    "ім'я": "Олексій",
    "вік": 25,
    "факультет": "Інформатика"
}

print("\nСловник студента:")
print("Ім'я:", student["ім'я"])
print("Вік:", student["вік"])

student["рік навчання"] = 2
print("Оновлений словник:", student)

try:
    num1 = int(input("\nВведіть перше число: "))
    num2 = int(input("Введіть друге число: "))
    result = num1 / num2
    print(f"Результат ділення: {result}")
except ZeroDivisionError:
    print("Помилка: Ділення на нуль неможливе!")
except ValueError:
    print("Помилка: Ви повинні ввести числа!")
