from task_4 import is_sorted
import random

print("************ Завдання 5 *******************")

# Завдання 5. Створіть функцію, яка замінює значення кожного елемента цілочисельного масиву сумою значення цього
# елемента та його індекса, лише якщо даний масив відсортовано в заданому порядку (порядок встановлюється за значенням
# словника {0: 'ascending', 1: 'descending'}).


def replace_sum(arr, sorting_order):
    if is_sorted(arr, sorting_order):
        replaced_arr = [x + i for i, x in enumerate(arr)]
        print("Масив замінено на:", replaced_arr)


if __name__ == "__main__":
    N = int(input("Введіть значення N: "))

    random_numbers = [random.randint(1, 100) for _ in range(N + 5)]
    ascending_array = sorted(random_numbers)
    descending_array = sorted(random_numbers, reverse=True)

    print("Вхідний не відсортований масив випадкових чисел: ", random_numbers)
    sorting_order = int(input("Ведіть порядок сортування: "))
    replace_sum(random_numbers, sorting_order)

    print()
    print("*******************************************")
    print()

    print("Вхідний, відсортований у порядку зростання, масив випадкових чисел: ", ascending_array)
    sorting_order = int(input("Ведіть порядок сортування: "))
    replace_sum(ascending_array, sorting_order)

    print()
    print("*******************************************")
    print()

    print("Вхідний, відсортований у порядку спадання, масив випадкових чисел: ", descending_array)
    sorting_order = int(input("Ведіть порядок сортування: "))
    replace_sum(descending_array, sorting_order)

    print()
    print("*******************************************")
    print()