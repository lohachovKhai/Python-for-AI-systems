import random

# Завдання 4. Створити функцію, яка визначає, чи є заданий масив довжини N+5 цілими значеннями, які відсортовані
#             в заданому порядку (порядок встановлюється за значенням словника {0: 'ascending', 1: 'descending'}).

def is_sorted(arr, sorting_order):
    n = len(arr)
    flag = False

    match sorting_order:
        case 0:
            check_ascending = lambda: all(arr[i] <= arr[i + 1] for i in range(n - 1))

            if check_ascending():
                print("Масив відсортований в порядку зростання.")
                flag = True
            else:
                print("Масив не відсортований в порядку зростання.")

        case 1:
            check_descending = lambda : all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

            if check_descending():
                print("Масив відсортований в порядку спадання.")
                flag = True
            else:
                print("Масив не відсортований в порядку спадання.")

        case _:
            raise ValueError("Невірний порядок сортування. Використовуйте 0 для 'ascending' або 1 для 'descending'.")

    return flag

if __name__ == "__main__":
    print("************ Завдання 4 *******************")

    N = int(input("Введіть значення N: "))

    random_numbers = [random.randint(1, 100) for _ in range(N + 5)]
    ascending_array = sorted(random_numbers)
    descending_array = sorted(random_numbers, reverse=True)


    print("Вхідний не відсортований масив випадкових чисел: ", random_numbers)
    sorting_order = int(input("Ведіть порядок сортування: "))
    is_sorted(random_numbers, sorting_order)

    print()
    print("*******************************************")
    print()

    print("Вхідний не відсортований масив випадкових чисел: ", random_numbers)
    sorting_order = int(input("Ведіть порядок сортування: "))
    is_sorted(random_numbers, sorting_order)

    print()
    print("*******************************************")
    print()

    print("Вхідний, відсортований у порядку зростання, масив випадкових чисел: ", ascending_array)
    sorting_order = int(input("Ведіть порядок сортування: "))
    is_sorted(ascending_array, sorting_order)

    print()
    print("*******************************************")
    print()

    print("Вхідний, відсортований у порядку спадання, масив випадкових чисел: ", descending_array)
    sorting_order = int(input("Ведіть порядок сортування: "))
    is_sorted(descending_array, sorting_order)

    print()
    print("*******************************************")
    print()