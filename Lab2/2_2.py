import random

from klas_menu import Menu

def bin_ser(elem_find):
    elem_find = int(elem_find)
    global _GLOBAL_array
    left, right = 0, len(_GLOBAL_array) - 1

    while left < right:
        mid = (left + right) // 2
        if elem_find == _GLOBAL_array[mid]:
            return mid
        elif _GLOBAL_array[mid] < elem_find:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def lin_ser(elem_find):
    elem_find = int(elem_find)
    global _GLOBAL_array
    for i in range(len(_GLOBAL_array)):
        if _GLOBAL_array[i]==elem_find:
            return i
    return -1

def pr_binary(elem_find):
    print(f'бинарный поиск, номер элемента = {bin_ser(elem_find)}')

def pr_line(elem_find):
    print(f'Линейный поиск, номер элемента= {lin_ser(elem_find)}')

_GLOBAL_array=[random.randint(-99,99) for _ in range(25)]
_GLOBAL_array.sort()

def genmas():
    global _GLOBAL_array
    _GLOBAL_array = [random.randint(-99,99) for _ in range(25)]
    _GLOBAL_array.sort()
    print(_GLOBAL_array)

def show():
    global _GLOBAL_array
    print(_GLOBAL_array)


if __name__ == '__main__':
    func = [genmas,show, pr_line, pr_binary]
    menu = Menu(
        numolabo=2.2,
        funcs=func
                )
    menu.start()
