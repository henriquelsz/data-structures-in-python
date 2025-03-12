from abc import ABC, abstractmethod

class INode(ABC): #interface class of Node
    @property
    @abstractmethod
    def value(self):
        pass
    
    @property
    @abstractmethod
    def next(self):
        pass

class Node(INode): #Node implements interface
    def __init__(self, value):
        self.__value = value
        self.__next = None

    @property
    def value(self):
        return self.__value #getter to value

    @property    
    def next(self):
        return self.__next #getter to next

    @next.setter
    def next(self, node):
        self.__next = node #setter to next

class Stack:

    def __init__(self):
        self.head: INode = Node("head")
        self.size = 0
    
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + '->'
            cur = cur.next
        return out[:-2]
    
    def get_size(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def top_value(self):
        if self.is_empty(self):
            return None
        
        return self.head.next.value
    
    def push(self, value):
        node = Node(value)
        node.next = self.head.next  # Atribuindo o próximo nó
        self.head.next = node  # Atualizando a referência do head
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Empty stack, can not pop")
        
        #It's possible to do an inplace memory option, just not initialize the remove variable and doesn't need to return something
        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1
        return remove.value 
'''
YOU can Uncomment this code snippet to run a Stack example

if __name__ == "__main__":
    stack = Stack()

    for i in range(1, 6):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 3):
        top_value = stack.pop()
        print(f"Pop: {top_value}")
    print(f"Stack: {stack}")
'''

    