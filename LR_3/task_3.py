print("************ Завдання 3 *******************")
# Завдання 3. Створити функцію, яка визначає суму перших елементів зменшуваної геометричної прогресії дійсних чисел
#             із заданим початковим елементом прогресії a(1) та даним кроком прогресії t, тоді як останній елемент
#             повинен бути більше заданого аlim.

def decreasing_geometric_progression_sum(a_1, alim, t):
    current_term = a_1
    total_sum = 0
    progression_elements =[]

    while current_term > alim:
        progression_elements.append(current_term)
        total_sum += current_term
        current_term *= t

    print(f"Масив елементів прогресії: {progression_elements}")
    return total_sum

a_1 = float(input("Введіть початковий елемент прогресії а: "))
a_lim = int(input("Введіть значення ліміту a_lim: "))
t = float(input("Введіть крок прогресії t: "))

sum_result = decreasing_geometric_progression_sum(a_1, a_lim, t)
print(f"Сума перших елементів, більших за {a_lim}, дорівнює {sum_result}")

print("*******************************************")
