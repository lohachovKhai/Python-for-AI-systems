print("************ Завдання 2 *******************")
# Завдання 2. Створити функцію, яка визначає множення перших q елементів арифметичної прогресії дійсних
#             чисел із заданим початковим елементом прогресії a(1) та кроку прогресування t.

def progression_counter(a_1, t, q):
    result = 1
    current_term = a_1
    progression_elements =[]

    for _ in range(q):
        progression_elements.append(current_term)
        result *= current_term
        current_term += t
    print(f"Масив елементів прогресії: {progression_elements}")
    return result

a_1 = float(input("Введіть початковий елемент прогресії а: "))
t = float(input("Введіть крок прогресуваня t: "))
q = int(input("Введіть значення кількості елементів прогресії q: "))

res = progression_counter(a_1, t, q)

print(f"Результат добутку {q} елементів прогресії: {res}")

print("*******************************************")