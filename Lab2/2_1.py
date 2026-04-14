from klas_menu import Menu

descript=[
    '4. Реализуйте рекурсивный алгоритм возведения в степень. Оцените сложность алгоритма.',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    ''
]
def rek_fibonachi(f,a=0,b=1,n=1): #f - номер искомого члена последовательности
    f = int(f)
    print(a,end=' ')
    if f!=n:
        rek_fibonachi(f,b,a+b,n+1)
    return 0

def just_fibonachi(f,a=0,b=1):
    f= int(f)
    for _ in range(f):
        print(a,end=' ')
        a,b = b,a+b

def rek_YMnojenie(a,b): #Работает лишь для целых, есть идея как сделать и для плавающих но это много 'костылей' со строками
    a=int(a); b=int(b)
    if b==0 or a==0 :
        return 0
    if b<0:
        return -rek_YMnojenie(a,-b)
    if b%2 == 0:
        return rek_YMnojenie(a<<1, b>>1)
    else:
        return a+rek_YMnojenie(a,b-1)

def just_YMnojenie(a,b):
    a = int(a)
    b = int(b)
    result = 0
    flag = False
    if b==0 or a==0:
        return 0
    if b<0:
        flag = True
        b=-b
    while b:
        if b%2:
            result += a
            b-=1
        else:
            a=a<<1
            b=b>>1
    if flag:
        result = -result
    return result

def rek_factorial(n):
    n = int(n)
    if n==0:
        return 1
    return n*rek_factorial(n-1)

def just_factorial(n):
    n = int(n)
    result = 1
    if n<0 or n!=int(n):
        print('idiot!')
        raise ValueError('idiot! x2')
    if n==0:
        return 1
    while n:
        result *= n
        n -= 1
    return result

def newton_10koren(S,epsilon=1e-15,max_iter=1000):
    if S<0 :
        raise ValueError('Корень из отрицательного числа')
    if S==0:
        return 0

    x=S if S<1 else S/10
    for _ in range(max_iter):
        x_new=(9*x+S/rek_stepen(x,9))/10
        if abs(x_new-x)<epsilon*max(1.0,abs(x)):
            return x_new
        x=x_new
    raise RuntimeError("Не сошлось за макс кол-во итераций")

def rek_stepen(a, n):
    a = float(a); n = float(n)
    if n==0 : #a в 0 степени = 1
        return 1
    elif n==1 : #a в 1 степени = а
        return a
    elif n<0 :  #a в -n степени = 1/(a в n степени)
        return 1/rek_stepen(a, -n)
    elif int(n)==n: #Если степень целая - это просто степень
        if n%2==0:  #Если степень чётная возводим в квадрат
            buffer = rek_stepen(a, n/2)
            return buffer*buffer
        else:
            return a*rek_stepen(a, n-1)
    else:   #Если степень нецелая - это арифметический корень, пробую представить это в виде арифметического корня по 10 из числа в некоторой степени
        tens_in_stepen=0
        while n-int(n):
            n*=10
            tens_in_stepen+=1
        buffer = rek_stepen(a, n)

        for _ in range(tens_in_stepen):
            buffer= newton_10koren(buffer)
        return buffer

def just_stepen(a,n):
    a= float(a); n = float(n)
    result = 1
    MinusFlag=False
    if n==0 :
        return 1
    if n==1 :
        return a
    if n<0 :
        MinusFlag=True
        n=-n
    if n == int(n):
        while n:
            if n%2:
                result *= a
                n-=1
            else:
                a *=a
                n//=2
    else:
        tens_in_stepen = 0
        while n - int(n):
            n *= 10
            tens_in_stepen += 1
        while n:
            if n%2:
                result *= a
                n-=1
            else:
                a *= a
                n/=2

        for _ in range(tens_in_stepen):
            result = newton_10koren(result)
    if MinusFlag:
        result = 1/result
    return result


def rek_NOD(a,b):
    a = int(a); b = int(b)
    if b==0 :
        return abs(a)
    else:
        return rek_NOD(b,a%b)

def just_NOD(a,b):
    a = int(a); b = int(b)
    while b:
        a,b = b,a%b
    return abs(a)

def perv(a,b):
    print(rek_YMnojenie(a,b))

def vtor(a,b):
    print(just_YMnojenie(a,b))

def tret(a):
    print(rek_factorial(a))

def chet(a):
    print(just_factorial(a))

def pyatt(a,b):
    print(rek_stepen(a,b))

def shest(a,b):
    print(just_stepen(a,b))

def sem(a,b):
    print(rek_NOD(a,b))

def vosem(a,b):
    print(just_NOD(a,b))

if __name__=='__main__':
    #func=[perv,vtor,tret,chet,pyatt]
    func = [rek_fibonachi,just_fibonachi,perv,vtor,tret,chet,pyatt,shest,sem,vosem]
    menu = Menu(numolabo=2.1,funcs=func)
    menu.start()