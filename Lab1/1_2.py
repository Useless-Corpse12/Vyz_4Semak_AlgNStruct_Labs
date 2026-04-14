import math
import random
from klas_menu import Menu

description = ('1) Дана последовательность случайных чисел длиной n.'
               ' Выбросить из ряда те элементы, значение которых равно a и b. '
               'Вывести полученное, а затем его отсортировать '
               'в порядке возрастания величин.'
'\n2)Получить все сочетания из 10 элементов по 4 элемента в каждом.'
'\n3)Дано натуральное число n. Вычислить 1∙2+2∙3∙4+ ...n(n+1)....2n.'
'\n4)Выяснить, сколько положительных элементов '
'содержит матрица |аij|i,j=1,…n, если аij=cos(i**2+n).'
'\n5)Дан двумерный массив случайных чисел. '
'Все положительные элементы этого массива заменить на число (-2), '
'нули без изменений, а отрицательные разделить на наибольший элемент массива.')

def fst():
    n=int(input("Скок случайных элементов генерируем: "))
    strt_nums = [random.randint(1,199)-100 for _ in range(n)]
    print(strt_nums)
    a,b = int(input('Введите a : ')),int(input('Введите b : '))
    strt_nums=[new_nums  for new_nums in strt_nums if (new_nums!=a and new_nums!=b)]
    print(strt_nums)
    #пузыр
    for i in range(len(strt_nums)):
        for j in range(i+1,len(strt_nums)):
            if strt_nums[i]>strt_nums[j]:
                strt_nums[i],strt_nums[j] = strt_nums[j],strt_nums[i]

    print(strt_nums)

def snd():
    #33 to 127
    symb_mass = [chr(random.randint(33,127)) for _ in range(10)]
    print('Стартовый массив - ', symb_mass)
    s=0
    for i in range(10):
        for j in range(i+1,10):
            for k in range(j+1,10):
                for l in range(k+1,10):
                    s+=1
                    print(s,'|', symb_mass[i],symb_mass[j], symb_mass[k], symb_mass[l])

def thrd():
    flag = True
    while flag:
        try:
            n=int(input('Введите то самое натуральное n : '))
        except:
            print('ex : неверный тип данных!')
        finally:
            if n<=0 :
                print('Число должно быть натуральным!')
            else:
                flag = False
    summ=0
    for i in range(1, n+1) :
        halfsumm=1
        print('i', i)
        for j in range(i, 2*i+1) :
            halfsumm*=j
            print('j', j)
        summ+=halfsumm
    print(summ)

def frth():
    n=int(input('Введите n : '))
    matrix = [[math.cos(i**2+n) for i in range(n)] for _ in range(n)]
    col_otpt=''
    positive = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j]>0:
                positive += 1
                col_otpt+=f'\033[31m{str(matrix[i][j])[:4]}\033[0m '
            else:
                col_otpt+=f'{str(matrix[i][j])[:4]} '
        col_otpt+='\n'

    print(col_otpt)
    print('Положительных чисел : ',positive)


def fifth():
    trixma = [[random.randint(1,199)-100 for _ in range(10)] for _ in range(10)]

    summ=0
    for i in range(10):
        for j in range(10):
            if trixma[i][j]>0:
                print(f'\033[34m{(trixma[i][j]):6d}\033[0m',end=' | ')
            elif trixma[i][j]<0:
                print(f'\033[33m{(trixma[i][j]):6d}\033[0m', end=' | ')
            else:
                print(f'{0:6d}', end=' | ')

            summ+=trixma[j][i]
        print()


    summ/=100
    print(f'\nСреднее арифметическое : {summ}', end='\n\n')

    for i in range(10):
        for j in range(10):
            if trixma[i][j]>0:
                print(f'\033[34m{-2:6d}\033[0m',end=' | ')
            elif trixma[i][j]<0:
                print(f'\033[33m{(trixma[i][j]/summ):6.2f}\033[0m',end=' | ')
            else:
                print(f'{0:6d}',end=' | ')
        print()
        #┗┛┻
#    print('┗━━━━┻' + '━' * 9 + '┻' + ('━' * 8 + '┻') * 8 + '━' * 8 + '┛')

if __name__ == '__main__':
    menu = Menu(funcs = [fst,snd,thrd,frth,fifth],numolabo = 1.2,desc = description)
    menu.start()