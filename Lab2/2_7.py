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
        if index < 0 or index >= self.length:
            raise IndexError("Idiot")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value


    def dеl(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = None
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
           return "Empty"
        value = ''
        current = self.head
        while current:
            value += str(current.value)
            current = current.next
        return value

    def info(self):
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

    def IsEmpty(self):
        return self.length == 0

    def push(self, data):
        new_node = TwoSideNode(data)
        if self.IsEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def push_back(self, data):
        new_node = TwoSideNode(data)
        if self.IsEmpty():
            self.head = self.tail = new_node
        else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
        self.length += 1

    def get(self,position=1):
        if position > self.length or position == 0:
            raise IndexError("Idiot")

        if position < 0:
            return self.__getback(-position)

        position-=1

        current = self.head
        for _ in range(position):
            current = current.next
        return current.value

    def __getback(self, position):
        if position> self.length:
            raise IndexError("Idiot")
        position-=1

        current = self.tail
        for _ in range(position):
            current = current.prev
        return current.value

    def add(self, value, position=1):
        if position > self.length or position == 0:
            raise IndexError('Idiot')

        if position < 0:
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
            current.next = new_node
            self.length += 1

    def __addback(self, value, position):
        if position > self.length:
            raise IndexError('Idiot')
        return 0

        position -= 1

        if position == 0:
            self.pushback(value)
        else:
            current = self.tail
            for _ in range(position - 1):
                current = current.prev
            new_node = TwoSideNode(value)
            new_node.prev = current.prev
            current.prev = new_node
            self.length += 1

    def del(self, position=1):
        if position > self.length or position == 0:
            raise IndexError("IdiotDelError pos must be > length"+self.length+"position must be > 0, pos is ")
if __name__ == "__main__":
    ll = LinkedList()
    print(ll)
    ll.append(1)
    print(ll.pop())
    print(ll)
    for (i) in range(4):
        ll.append(i)

    print(ll)
    print(ll.get(3))
    print(ll.dеl(3))
    print(ll)
    print(ll.dеl(2))
    dll = DoubleLinkedList()
    dll.push(3)
    dll.push(2)
    dll.push(1)
    dll.push(4)
    dll.push(5)
    dll.push(6)
    #[321456]
    print(dll.get(1))
    #6
    print(dll.get(3))
    #1
    print(dll.get(-1))
    #5
    print(dll.get(-5))
    #3
    print(dll.get())
    print()
    dll.add(7,-2)
    for _ in range(7):
        print(dll.get(_+1))
