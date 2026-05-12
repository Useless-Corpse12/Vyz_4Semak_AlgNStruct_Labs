from klas_menu import Menu


class ADT:
    def info(self):
        print('\nАбстра́ктный тип да́нных (АТД) — это математическая модель для типов данных, '
              '\nгде тип данных определяется поведением (семантикой) с точки зрения пользователя данных, '
              '\nа именно в терминах возможных значений, возможных операций над данными этого типа и '
              '\nповедения этих операций.\n')

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LIFO_ADT(ADT):
    def __init__ (self):
        self._toplem = None
        self._size = 0

    def push(self,val):
        new_part = Node(val)
        new_part.next = self._toplem
        self._toplem = new_part
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError('idiot')
        value = self._toplem.value
        self._toplem=self._toplem.next
        self._size -= 1
        return value

    def peek(self):
        if self.isEmpty():
            raise IndexError('idiot')
        return self._toplem.value


    def isEmpty(self):
        return self._toplem is None

    def size(self):
        return self._size

    def __str__(self):
        values = []
        current = self._toplem
        while current:
            values.append((str(current.value))+' ')
            current = current.next

        return f"Jabik's Stack({values})"

    def info(self):
        print('\nСтек (МФА: /stɛk/) (англ. stack — стопка) — абстрактный тип данных, '
              '\nпредставляющий собой список элементов, организованных по принципу '
              '\nLIFO (англ. last in — first out, «последним пришёл — первым вышел»).\n')

class OneWayFIFA_ADT(ADT):
    def __init__(self):
        self._in_stack  = LIFO_ADT()
        self._out_stack = LIFO_ADT()

    def pop(self):
        if self.is_empty():
            raise IndexError('idiot')

        if self._out_stack.isEmpty():
            while not self._in_stack.isEmpty():
                self._out_stack.push(self._in_stack.pop())

        return self._out_stack.pop()

    def push(self, item):
        self._in_stack.push(item)

    def front(self):
        if self.is_empty():
            raise IndexError('idiot')

        if self._out_stack.isEmpty():
            while not self._in_stack.isEmpty():
                self._out_stack.push(self._in_stack.pop())

        return self._out_stack.peek()

    def is_empty(self):
        return self._in_stack.isEmpty() and self._out_stack.isEmpty()

    def size(self):
        return self._in_stack.size() + self._out_stack.size()

    def info(self):
        print('\nО́чередь — абстрактный тип данных с дисциплиной доступа к элементам '
              '\n«первый пришёл — первый вышел» (FIFO, англ. first in, first out).\n')

    def __str__(self): #DEBUG_ONLY
        if self.is_empty():
            return "empty"
        items = []
        current = self._out_stack._toplem
        while current:
            items.append(str(current.value) + ' ')
            current = current.next
        items.reverse()
        current = self._in_stack._toplem
        while current:
            items.append((str(current.value))+' ')
            current = current.next

        return f"Jabik's FIFO({items})"

class BothWayFIFA_ADT(OneWayFIFA_ADT):
    def pushback(self,item):
        self._out_stack.push(item)

    def popback(self):
        if self.is_empty():
            raise IndexError('idiot')

        if self._in_stack.isEmpty():
            while not self._out_stack.isEmpty():
                self._in_stack.push(self._out_stack.pop())

        return self._in_stack.pop()

    def frontback(self):
        if self.is_empty():
            raise IndexError('idiot')

        if self._in_stack.isEmpty():
            while not self._out_stack.isEmpty():
                self._in_stack.push(self._out_stack.pop())

        return self._in_stack.peek()

    def info(self):
        print('\nДвусвязная очередь (жарг. дэк, дек от англ. deque — double-ended queue; '
              '\nдвусторонняя очередь, очередь с двумя концами) — абстрактный тип данных, '
              '\nв котором элементы можно добавлять и удалять как в начало, так и в конец.\n')


def LIFO_Test():
    LIFO = LIFO_ADT()
    LIFO.info()
    funcs=[
        lambda *args: LIFO.push(args[0]),
        lambda:print(LIFO.pop()),
        lambda:print(LIFO.peek()),
        lambda:print(LIFO.isEmpty()),
        lambda:print(LIFO.size()),
        lambda:print(str(LIFO))]

    desc = ("1)push\n"
            "2)pop\n"
            "3)peek\n"
            "4)isEmpty?\n"
            "5)size\n"
            "6)LifoContainer")
    LifoMenu = Menu(funcs = funcs,desc=desc,numolabo=2.61,help=False)
    LifoMenu.start()
    return 0


def FIFA_Test():
    FIFA = OneWayFIFA_ADT()
    FIFA.info()
    funcs = [
        lambda *args: FIFA.push(args[0]),
        lambda: print(FIFA.pop()),
        lambda: print(FIFA.front()),
        lambda: print(str(FIFA.is_empty())),
        lambda: print(FIFA.size()),
        lambda: print(str(FIFA))]

    desc = ("1)push\n"
            "2)pop\n"
            "3)front\n"
            "4)isEmpty?\n"
            "5)size\n"
            "6)LifoContainer")

    FifaMenu = Menu(funcs=funcs, desc=desc, numolabo=2.62,help=False)
    FifaMenu.start()
    return 0


def DFIFA_Test():
    DFIFA = BothWayFIFA_ADT()
    DFIFA.info()
    funcs = [
        lambda *args: DFIFA.push(args[0]),
        lambda *args: DFIFA.pushback(args[0]),
        lambda:print(DFIFA.pop()),
        lambda:print(DFIFA.popback()),
        lambda:print(DFIFA.front()),
        lambda:print(DFIFA.frontback()),
        lambda:print(str(DFIFA.is_empty())),
        lambda:print(DFIFA.size()),
        lambda:print(str(DFIFA))]

    desc = ("1)push\n"
            "2)pushback\n"
            "3)pop\n"
            "4)popback\n"
            "5)front(peek)\n"
            "6)frontback(peek back)\n"
            "7)isEmpty?\n"
            "8)size\n"
            "9)LifoContainer")

    DFifaMenu = Menu(funcs=funcs, desc=desc, numolabo=2.63,help=False)
    DFifaMenu.start()
    return 0

if __name__ == '__main__':
    ADT = ADT()
    ADT.info()
    funcs = [LIFO_Test, FIFA_Test, DFIFA_Test]
    description = ("1)Работа со стеком(LIFO)\n"
                   "2)Работа с односторонней очередью\n"
                   "3)Работа с двусторонней очередью")
    Glob_MENU = Menu(funcs = funcs, desc = description, numolabo=2.6)
    Glob_MENU.start()

