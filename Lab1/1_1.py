import math
from klas_menu import Menu

description = ['1)Найти площадь равностороннего треугольника, зная длину стороны.',
               '2)Известна длина окружности. Найти площадь круга, ограниченного этой окружностью.)',
               '3)Даны числа a, b, c - основания, d, e, f – степени чисел. Определить, какое число в какой степени больше остальных чисел в аналогичной степени.',
               '4)Даны 5 чисел. Найти среди них такие три числа, чтобы их сумма была равна 7. Если таких чисел нет, то сообщить об этом.',
               '5)Определить, попадает ли точка в треугольную область, заданную в координатной форме']
def fst():
    print('Площадь равностороннего треугольника равна = '+str((float(input('Введите сторону треугольника : '))**2)*(3**(1/2))/4))

def snd():
    print('Площадь круга ограниченного окружностью = '+str(((float(input('Введите длину окуржности : '))/2)/math.pi)**2))

def thrd():
    nums = input('Введите 3 числа возводящиеся в степень : ').split()[:3]
    nums = [float(num) for num in nums]
    print(nums)
    grads = input('Введите 3 степени в которые возводятся числа : ').split()[:3]
    grads = [float(grad) for grad in grads]
    print(grads)

    for grad in grads:
        winner=2
        if nums[0]**grad >= nums[1]**grad and nums[0]**grad >= nums[2]**grad:
            winner=0
        elif nums[1]**grad >= nums[2]**grad and nums[1]**grad >= nums[0]**grad:
            winner=1
        print(f'Победитель в номинации самое большое число в степени {grad} становится {nums[winner]}')

def frth():
    nums = input('Введите 5 чисел : ').split()[:5]
    nums = [float(num) for num in nums]
    n=len(nums)
    flag = True
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==7:
                    flag=False
                    print(f'({nums[i]}) + ({nums[j]}) + ({nums[k]}) = 7')
    if flag:
        print('Нет таких чисел')

def ffth():
    p1=[1,1]
    p2=[1,10]
    p3=[10,10]
    print(f'Дан треугольник с точками {p1},{p2},{p3}')
    pu=float(input('Введите x : ')),float(input('Введите y : '))
    d1=ffthaddition(pu,p1,p2)
    d2=ffthaddition(pu,p2,p3)
    d3=ffthaddition(pu,p3,p1)

    if ((d1<0 or d2<0 or d3<0)and(d1>0 or d2>0 or d3>0)):
        print("Точка вне треугольника")
    else:
        print("Точка в треугольнике")

def ffthaddition(p1,p2,p3):
    return (p1[0]-p3[0])*(p2[1]-p3[1])-(p2[0]-p3[0])*(p1[1]-p3[1])


if __name__ == '__main__':
    menu=Menu([fst,snd,thrd,frth,ffth],1.1,desc = description)
    menu.start()
