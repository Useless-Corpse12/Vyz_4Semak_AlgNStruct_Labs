import os
import timeit
from contextlib import redirect_stdout


class Menu:
    def __init__(self,funcs,numolabo=0,desc=None, help = True,globmenu=True):
        self.funcs=funcs
        self.numolabo=numolabo
        if desc is None:
            self.description=[f'{n+1}' for n in range(len(funcs))]
        elif type(desc) is list :
            self.description=desc
        elif type(desc) is str :
            self.description=desc.split('\n')
        self.__comparelist = []
        self.__iscompare = True
        self.__numo = 10
        self.__repo = 10
        self.__rejimo = 2
        self.last_err = 'Пока ошибок не было. Счастливчик...'
        self.__help = help
        self.globmenu = globmenu


    def __time_zamer(self,com):
        try:
            funconumo = int(com[1])
            comparestring = self.description[funconumo - 1]

            if len(com) > 2:
                args = com[2:]
                ftt = lambda: self.funcs[funconumo - 1](*args)
            else:
                ftt = lambda: self.funcs[funconumo - 1]

            with open(os.devnull, 'w') as devnull, redirect_stdout(devnull):
                timer = timeit.Timer(ftt)
                times = timer.repeat(repeat=self.__repo, number=self.__numo)
            smin = f'\nМинимальное время выполнение функции {min(times)}ms'
            atime = f'\nСреднее время выполнение функции {sum(times) / len(times)}ms'

            if self.__rejimo == 0:
                print(smin)
                comparestring += smin
            elif self.__rejimo == 1:
                print(atime)
                comparestring += atime
            else:
                print(smin + atime)
                comparestring += smin + atime + '\n'
            if self.__iscompare:
                self.__comparelist.append(comparestring)
        except Exception as e:
            self.last_err = f'{type(e).__name__}: {e}'
            print('zamer is failed. dont cringe next time')


    def __changing_zamer_config(self,com):
        try:
            if com[1] != '*':
                self.__numo = int(com[1])
            if com[2] != '*':
                self.__repo = int(com[2])
            if com[3] != '*':
                self.__rejimo = int(com[3])
            if com[4] != '*':
                self.__iscompare = bool(com[4])
        except Exception as e:
            self.last_err = f'{type(e).__name__}: {e}'
            print('efficiency config changing error')


    def __function_work(self,com,message):
        try:
            a = int(com[0])
            if 0 < a <= len(self.funcs):
                if self.globmenu:
                    print('━' * (message - 1) + '┓' + '\n' + ' ' * (message // 2 - 7) + f'Задание #{a:3}' + ' ' * (
                            message // 2 - 6) + '┃\n' + '━' * (message - 1) + '┛')
                print()
                print(self.description[a - 1])
                print('\n::>>Консольный вывод<<::\n')
                try:
                    if len(com) <= 1:
                        self.funcs[a - 1]()
                    else:
                        args = com[1:]
                        self.funcs[a - 1](*args)
                except Exception as e:
                    self.last_err = f'{type(e).__name__}: {e}'
                    print(f'Произашла ошибка с выполнением {a} задания')
            else:
                for i in range(len(self.funcs)):
                    if self.globmenu:
                        print('━' * (message - 1) + '┓' + '\n' + ' ' * (message // 2 - 7) + f'Задание #{i + 1:3}' + ' ' * (
                                message // 2 - 6) + '┃\n' + '━' * (message - 1) + '┛')
                    print()
                    print(self.description[i])
                    print('\n::>>Консольный вывод<<::\n')
                    try:
                        if len(com) <= 1 or com[1] is None:
                            self.funcs[i]()
                        else:
                            self.funcs[i](com[1])
                    except Exception as e:
                        self.last_err = f'{type(e).__name__}: {e}'
                        print(f'Произашла ошибка с выполнением {i + 1} задания')
                    print()
        except Exception as e:
            self.last_err = f'{type(e).__name__}: {e}'
            print('Команда неверно распознана, или произошла непредвиденная ошибка!')

    def start(self):
        cl = ('\n       ::::>>COMMAND LIST<<::::'
                      '\n\'exept\'                  ::> Вывод последней ошибки'
                      '\n\'efh\'                    ::> Справка для команд по замеру функций'
                      '\n\'effconf\'                ::> Изменение параметров замеров'
                      '\n\'eff\' \'*номер*\' \'*параметр*\'       ::> Замер функции с входными параметрами(опционально)'
                      '\n\'*номер*\' \'*параметр*\'   ::> Запуск функции с входными параметрами(опционально)'
                      '\n\'cmp\'                    ::> Выводит список сравнения'
                      '\n\'cmpc\'                   ::> Очищает список сравнения'
                      '\n\'exit\'                   ::> Завершение работы меню \n\n')
        fio='Студент группы, Вариант №16 '
        stroka = 64
        message = 48
        if self.__help:
            print(cl)
        print('━'*(stroka-1)+'┓')
        print(' '*((stroka-len(fio))//2) + fio + ' '*((stroka-len(fio))//2 - 1)+'┃')
        print('━'*(message-1)+'┳'+'━'*(stroka-message-1)+'┛')
        print(' '* (message//2 - 5)+f'Лаба #{self.numolabo:3.3f}'+' '*(message//2 -7)+'┃')
        print('━'*(message-1)+'┛\n')

        for el in self.description:
            print(el)

        print('\nВведите номер задания : ')
        while True:
            com=input('>').lower().split(' ')
            if com[0]=='exit':
                return
            elif com[0]=='help':
                print(cl)

            elif com[0]=='exept':
                print(self.last_err)

            elif com[0]=='cmp':
                if len(self.__comparelist)>0:
                    for elem in self.__comparelist:
                        print(elem)
                else:
                    print('Список пуст')

            elif com[0]=='cmpc':
                self.__comparelist.clear()

            elif com[0]=='efh':
                print(f'\n!For Efficiency testing! ::> \'eff\' ex_num input(if need)\n!For changing config! ::> \'effconf\' num repeats mode compare_list_adding'
                      f'\n::>>(now values, num={self.__numo}, repeats={self.__repo}, mode={self.__rejimo}, is_add_to_compare?={self.__iscompare})<<::'
                      f'\n!place \'*\' if u dont need to change the value!'
                      f'\n(smth like ::> effconf 20 * * *)')

            elif com[0]=='effconf':
                self.__changing_zamer_config(com)

            elif com[0]=='eff':
                self.__time_zamer(com)
            else:
                self.__function_work(com,message)
            print()
            for el in self.description:
                print(el)


def koseno():
    print(bool('0'),bool(0),bool(''),bool(' '))

if __name__ == '__main__':
    menu=Menu([koseno],2)
    menu.start()