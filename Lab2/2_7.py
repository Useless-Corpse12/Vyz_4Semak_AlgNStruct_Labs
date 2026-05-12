from klas_menu import Menu



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0


    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.length = 1
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
            self.length += 1

    def add(self, data,index):
        index =int(index)
        if index < 0 or index > self.length:
            raise IndexError("Idiot")

        if index == 0:
            self.push(data)
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def get(self, index):
        index = int(index)
        if index < 0 or index >= self.length:
            raise IndexError("Idiot")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value


    def dеl(self, index):
        index = int(index)
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.length -= 1
        return True


    def getsize(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    def front(self):
        if self.isEmpty():
            return None
        else:
            return self.head.value

    def pop(self):
        if self.isEmpty():
            return None
        else:
            self.length -= 1
            val = self.head.value
            self.head = self.head.next
            return val

    def __str__(self):
        if self.isEmpty():
           return "[Empty]"
        current = self.head
        value = 'head > [' + str(current.value)
        current = current.next
        while current:
            value += f',{current.value}'
            current = current.next
        value += ']'
        return value

    @staticmethod
    def info():
        print('Линейный однонаправленный список — это структура данных, состоящая из элементов одного типа, '
              '\nсвязанных между собой последовательно посредством указателей. '
              '\nКаждый элемент списка имеет указатель на следующий элемент. '
              '\nПоследний элемент списка указывает на NULL. '
              '\nЭлемент, на который нет указателя, является первым (головным) элементом списка.'
              '\nФункции : \nПроверка на пустоту\nВзять элемент по индексу\nВставить по индексу\nУдалить по индексу')

class TwoSideNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


#Double Linked List
# n1 position != 0, n1 position == 1
#[...,n4,n3,n2,n1]
#<-tail     head->
#<-next     prev->

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def push(self, data):
        new_node = TwoSideNode(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def pushback(self, data):
        new_node = TwoSideNode(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
        self.length += 1

    def pop(self):
        if self.isEmpty():
            return None

        val = self.head.value

        self.length -= 1

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return val

    def popback(self):
        if self.isEmpty():
            return None

        val = self.tail.value

        self.length -= 1

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return val

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.value

    def peekback(self):
        if self.isEmpty():
            return None
        else:
            return self.tail.value

    def get(self,position=1):
        position = int(position)
        if position > self.length or position == 0:
            raise IndexError(f'DoubleLinkedlist get error. params : pos = {position}, length = {self.length}')

        if position < 0:
            return self.__getback(-position)

        current = self.head
        for _ in range(position-1):
            current = current.next
        return current.value

    def __getback(self, position):
        if position> self.length:
            raise IndexError(f'DoubleLinkedlist __getback error. params : pos = {position}, length = {self.length}')

        current = self.tail
        for _ in range(position-1):
            current = current.prev
        return current.value

    def add(self, value, position=1):
        position = int(position)
        if position==self.length:
            new = self.popback()
            self.pushback(value)
            self.pushback(new)
            return 0
        elif position > self.length or position == 0:
            raise IndexError(f'DoubleLinkedlist back error. params : pos = {position}, length = {self.length}')
        elif position < 0:
            return self.__addback(value,-position)

        position-=1

        if position == 0:
            self.push(value)
        else:
            current = self.head
            for _ in range(position-1):
                current = current.next

            new_node = TwoSideNode(value)
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            self.length += 1


    def __addback(self, value, position):
        if position==self.length:
            new = self.pop()
            self.push(value)
            self.push(new)
            return 0
        elif position > self.length:
            raise IndexError(f'DoubleLinkedlist __addback error. params : pos = {position}, length = {self.length}')

        position -= 1

        if position == 0:
            self.pushback(value)
        else:
            current = self.tail
            for _ in range(position - 1):
                current = current.prev

            new_node = TwoSideNode(value)
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            self.length += 1

    def dеl(self, position=1):
        position = int(position)
        if position > self.length or position == 0:
            raise IndexError(f'DoubleLinkedlist del error. params : pos = {position}, length = {self.length}')
        if position<0:
            return self.__dеlback(-position)
        position-=1

        if position == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        else:
            curr = self.head
            for _ in range(position - 1):
                curr = curr.next
            curr.next = curr.next.next
            if curr.next:
                curr.next.prev = curr
            else:
                self.tail = curr

        self.length -= 1

    def __dеlback(self,position):
        if position > self.length or position == 0:
            raise IndexError(f'DoubleLinkedlist __delback error. params : pos = {position}, length = {self.length}')
        position-=1

        if position == 0:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            curr = self.tail
            for _ in range(position - 1):
                curr = curr.prev
            curr.prev = curr.prev.prev
            if curr.prev:
                curr.prev.next = curr
            else:
                self.head = curr

        self.length -= 1

    def getsize(self):
        return self.length

    def __str__(self):
        if self.isEmpty():
           return "[Empty]"
        current = self.head
        value = 'head > ['+str(current.value)
        current = current.next
        while current:
            value += f',{current.value}'
            current = current.next
        value += '] < tail'
        return value

    @staticmethod
    def info():
        print('Двусвязный (двунаправленный) список — это динамическая структура данных,\n'
              'состоящая из узлов, каждый из которых содержит данные и две ссылки:\n'
              'на следующий и предыдущий узлы. В отличие от односвязного списка,\n'
              'здесь возможно перемещаться по списку в обоих направлениях —\n'
              'как вперёд, так и назад.')


def sll_test():
    sll = LinkedList()
    sll.info()
    func = [
        lambda *args: sll.push(args[0]),
        lambda *args: sll.append(args[0]),
        lambda *args: sll.add(args[0],args[1]),
        lambda *args: print(sll.get(args[0])),
        lambda *args: sll.dеl(args[0]),
        lambda:print(sll.pop()),
        lambda:print(sll.front()),
        lambda:print(sll.getsize()),
        lambda:print(sll.isEmpty()),
        lambda:print(str(sll))
    ]
    descritption = ("1)push   *v    - добавляет элемент(v) в начало\n"
                    "2)append *v    - добавляет элемент(v) в конец\n"
                    "3)add    *v *i - добавляет элемент(v) вслед за индексом(i)\n"
                    "4)get    *i    - возвращает элемент с определенным индексом(i)\n"
                    "5)del    *i    - удаляет элемент с определённым индексом(i)\n"
                    "6)pop          - возвращает головной элемент(с удалением)\n"
                    "7)front        - возвращает головной элемент(лишь значение\n"
                    "8)getsize      - возвращает длинну массива\n"
                    "9)isEmpty      - проверяет массив на пустоту\n"
                    "10)вывод массива")

    sll_menu = Menu(desc=descritption,funcs=func,numolabo=2.71,globmenu=False)
    sll_menu.start()

def dll_test():
    dll = DoubleLinkedList()
    dll.info()

    func = [
        lambda *args:dll.push(args[0]),
        lambda *args:dll.pushback(args[0]),
        lambda *args:dll.add(args[0],args[1]),
        lambda *args:print(dll.get(args[0])),
        lambda *args:dll.dеl(args[0]),
        lambda:print(dll.pop()),
        lambda:print(dll.popback()),
        lambda:print(dll.peek()),
        lambda:print(dll.peekback()),
        lambda:print(dll.getsize()),
        lambda:print(dll.isEmpty()),
        lambda:print(str(dll)),
    ]

    descritption=("01)push   *v    - добавляет элемент(v) в начало\n"
                "02)pushback *v    - добавляет элемент(v) в конец\n"
                "03)add      *v *i - добавляет элемент(v) вслед за индексом(i)\n"
                "04)get      *i    - возвращает элемент с определенным индексом(i)\n"
                "05)del      *i    - удаляет элемент с определённым индексом(i)\n"
                "06)pop            - возвращает головной элемент(с удалением)\n"
                "07)popback        - возвращает хвостовой элемент(с удалением)\n"
                "08)peek           - возвращает головной элемент(лишь значение\n"
                "09)peekback       - возвращает хвостовой элемент(лишь значение\n"
                "10)getsize        - возвращает длинну массива\n"
                "11)isEmpty        - проверяет массив на пустоту\n"
                "12)вывод массива")

    dll_menu = Menu(desc=descritption,funcs=func,numolabo=2.72,globmenu=False)
    dll_menu.start()

if __name__ == "__main__":
    func = [sll_test, dll_test]
    descritption = ("1)Работа с односвязным списком (*v - (данные) *i - (индекс)) (0-based)\n"
                    "2)Работа с двусвязным списком  (*v - (данные) *i - (индекс(в том числе реверсивный))) (1-based)")
    glob_menu = Menu(funcs=func,desc=descritption,numolabo=2.7)
    glob_menu.start()