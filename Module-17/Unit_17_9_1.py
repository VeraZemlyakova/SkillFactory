import random

class MyExCount(Exception):
    pass

class MyExRange(Exception):
    pass

def num_range(num):
    if not all([num >= 0, num <= 100]):
        raise MyExRange
    else:
        return num

def out_red(text):
    print("\033[31m{}".format(text), "\033[0;0m")

def input_point():
    while True:
        try:
            #f = -1 f = 0 f = 1 f = 5 f= 20 f = 52 f = 65 f = 99 f = 100 f = 101 f = 105
            f = int(input("Введите любое целое число:\t"))
        except Exception:
            out_red("Введенное значение не является целым числом.")
        else:
            return f

def out_result(pos):
    if pos[0] is None:
        if arr[pos[1]] > point:
            print(f"В списке есть элемент '{arr[pos[1]]}' больше '{point}', но нет элемента меньше '{point}'")
        else:
            print(f"В списке есть элемент '{point}', но нет элемента меньше '{point}'")
    elif pos[1] is None:
        print(f"В списке есть элемент '{arr[pos[0]]}' меньше '{point}', но нет элемента больше или равного '{point}'")
    else:
        if arr[pos[1]] > point:
            #        print("\033[34m{}".format(text), "\033[0;0m")
            print(f"Позиция элемента списка '{arr[pos[0]]}', который меньше '{point}',"
                  f" а следующий за ним '{arr[pos[1]]}' больше '{point}':\t", "\033[34m{}".format(pos[0]), "\033[0;0m")
        else:
            print(f"Позиция элемента списка '{arr[pos[0]]}', который меньше '{point}',"
                  f" а следующий за ним '{arr[pos[1]]}' равен '{point}':\t", "\033[34m{}".format(pos[0]), "\033[0;0m")

def merge(left, right):
    i, j, res = 0, 0, [] # указатели на элементы и результирующий массив
    while True:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
            if i == len(left):
                res.extend(right[j:])
                break
        else:
            res.append(right[j])
            j += 1
            if j == len(right):
                res.extend(left[i:])
                break
    return res

def bottom_up_merge_sort(array):
    k = 1
    while k < len(array):
        for i in range(0, len(array)-k, 2*k):
            array[i:i+2*k] = merge(array[i:i+k], array[i+k:i+2*k])
        k *= 2
    return array

def binary_search(array, point, left, right):
    middle = (right + left) // 2  # находим середину
    if array[middle] >= point:  # если элемент в середине, больше или равен введенному числу
        if middle == left:  # достигнута левая граница списка
            return None, middle
        elif array[middle-1] < point:  # предыдущий элемент меньше введенного числа
            return middle-1, middle
        else:
            return binary_search(array, point, left, middle - 1)  # ищем в левой части
    elif array[middle] < point:  # если элемент в середине, меньше введенного числа
        if middle == right:  # достигнута правая граница списка
            return middle, None
        elif array[middle + 1] >= point:  # следующий элемент больше или равен введенному числу
            return middle, middle+1
        else:
            return binary_search(array, point, middle + 1, right)  # ищем в правой части

while True:
    try:
#       arr = [67, 52, 10, 20, 32, 52, 58, 62, 63, 64, 37, 67, 52, 83, 20, 88, 20, 6]
        arr = list(random.randint(0, 100) for i in range(0, random.randint(10, 20)))  # генератор списка натуральных чисел
#       arr = list(map(num_range, map(int, input("Введите последовательность целых чисел от 0 до 100 через пробел:\t").split())))
        if len(arr) < 2:
            raise MyExCount
    except MyExRange:
        out_red('Одно или несколько чисел выходят за пределы диапазона от 0 до 100.')
    except MyExCount:
        out_red('Последовательность должна содержать не менее двух чисел.')
    except Exception:
        out_red("Одно или несколько введенных чисел не являюся целыми числами.")
    else:
        print("Последовательность чисел:\t", *arr)
        point = input_point()  # запрашивается у пользователя любое целое число
        print("Отсортированный список:\t", bottom_up_merge_sort(arr))
        out_result(binary_search(arr, point, 0, len(arr) - 1))
#       print(dict(enumerate(bottom_up_merge_sort(arr))))
        break

