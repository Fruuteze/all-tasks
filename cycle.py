# Задание №1

a_1 = int(input("Введите первый член прогрессии: "))
n = int(input("Введите количество членов прогрессии: "))

# Выбор режима работы программы
while True:
    mode = input("Выберите режим работы: 1 - формулы, 2 - циклы\n")
    if mode == "1" or mode == "2":
        break
    else:
        print("Ошибка ввода, попробуйте еще раз")

if mode == "1":
    # Формулы
    q = int(input("Введите знаменатель прогрессии: "))
    # Сумма арифметической прогрессии
    s_arith = (a_1 + a_1 + (n - 1)*q) * n / 2
    # Сумма геометрической прогрессии
    s_geom = a_1 * (1 - q**n) / (1 - q)

    print("Сумма арифметической прогрессии:", s_arith)
    print("Сумма геометрической прогрессии:", s_geom)

else:
    # Циклы
    if n == 1:
        s_arith = a_1
        s_geom = a_1
    else:
        s_arith = 0
        s_geom = 0
        q = int(input("Введите знаменатель прогрессии: "))
        # Сумма арифметической прогрессии
        for i in range(n):
            a_i = a_1 + i*q
            s_arith += a_i
        # Сумма геометрической прогрессии
        for i in range(n):
            a_i = a_1*q**i
            s_geom += a_i

        print("Сумма арифметической прогрессии:", s_arith)
        print("Сумма геометрической прогрессии:", s_geom)

№2


def binary_search(arr, x):
    """
    Функция бинарного поиска в отсортированном массиве.

    :param arr: Отсортированный массив для поиска.
    :param x: Значение для поиска.
    :return: True, если значение найдено, False в противном случае.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Тестирование функции
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5
if binary_search(arr, x):
    print("True")
else:
    print("False")