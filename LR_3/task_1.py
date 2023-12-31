print("************ Завдання 1 *******************")
# Завдання 1. Для цілого додатного числа N обчисліть значення результату, що дорівнює сумі "1" у двійковому поданні числа N

def count_bits(n):
    count = 0
    while n > 0:
        count += n & 1  # Перевірка останнього біту
        n >>= 1         # Зсув вправо на 1 біт
    return count

N = int(input("Введіть ціле додатнє число N: "))

result = count_bits(N)
binary_representation = bin(N)[2:]  # Перетворення в двійковий рядок та видалення префіксу '0b'

print(f"Двійкове подання числа {N}: {binary_representation}")
print(f"Сума '1' в двійковому поданні числа {N} дорівнює:  {result}")

print("*******************************************")