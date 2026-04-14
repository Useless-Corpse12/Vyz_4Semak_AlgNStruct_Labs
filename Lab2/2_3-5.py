import random

from klas_menu import Menu

descript = ('Перемешываем массивчик'
            '\nПоказываем массивчик'
            '\n1)Сортировка вставками'
            '\n2)Сортировка выбором'
            '\n3)Сортировка пузырьком'
            '\n4)Сортировка Шелла'
            '\n5)Сортировка слиянием'
            '\n6)Быстрая сортировка')

def III_Insert(massive):
    if len(massive) <=1:
        return massive

    for i in range(1,len(massive)):
        key=massive[i]
        j=i-1

        while j>=0 and key<massive[j]:
            massive[j+1]=massive[j]
            j-=1

        massive[j+1]=key

    return massive

def III_Select(massive):
    if len(massive) <=1:
        return massive

    for i in range(len(massive)):
        minpos=i
        for j in range(i+1,len(massive)):
            if massive[j] < massive[minpos]:
                minpos = j
        massive[i],massive[minpos] = massive[minpos],massive[i]

    return massive

def IV_Bubble(massive):
    if len(massive)<=1:
        return massive

    for i in range(len(massive)-1):
        for j in range(i+1, len(massive)):
            if massive[i] > massive[j]:
                massive[i], massive[j] = massive[j], massive[i]
    return massive

def IV_Shel(massive):
    last_index = len(massive)
    step = len(massive) // 2

    while step > 0:

        for i in range(step, last_index, 1):
            j = i
            delta = j - step

            while delta >= 0 and massive[delta] > massive[j]:

                massive[delta], massive[j] = massive[j], massive[delta]
                j = delta
                delta = j - step

        step //= 2

    return massive


def V_Merge(massive):
    if len(massive) <= 1:
        return massive

    mid = len(massive) // 2
    left_half = massive[:mid]
    right_half = massive[mid:]

    left_half = V_Merge(left_half)
    right_half = V_Merge(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left or right)
    return merged



def V_Quick(massive):
    if len(massive) <= 1:
        return massive
    opora = massive[len(massive) // 2]
    left = [x for x in massive if x < opora]
    middle = [x for x in massive if x == opora]
    right = [x for x in massive if x > opora]
    return V_Quick(left) + middle + V_Quick(right)

_GLOBAL_array = []

def shuffle_array(n=25):
    n=int(n)
    global _GLOBAL_array
    _GLOBAL_array = [random.randint(-99,99) for _ in range(n)]
    print("Массив обновлен:", _GLOBAL_array)

def show_array():
    global _GLOBAL_array
    print(_GLOBAL_array)

def q_s():
    global _GLOBAL_array
    print(V_Quick(_GLOBAL_array[:]))

def m_s():
    global _GLOBAL_array
    print(V_Merge(_GLOBAL_array[:]))

def sh_s():
    global _GLOBAL_array
    print(IV_Shel(_GLOBAL_array[:]))

def b_s():
    global _GLOBAL_array
    print(IV_Bubble(_GLOBAL_array[:]))

def i_s():
    global _GLOBAL_array
    print(III_Insert(_GLOBAL_array[:]))

def s_s():
    global _GLOBAL_array
    print(III_Select(_GLOBAL_array[:]))

if __name__ == '__main__':
    shuffle_array()
    funcs=[shuffle_array,show_array, i_s, s_s, b_s,sh_s,m_s,q_s]
    menu = Menu(numolabo=2.345,funcs=funcs,desc=descript)
    menu.start()
