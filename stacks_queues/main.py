

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None



class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stck(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def stack_push(self, value):
        new_node = Node(value)  
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1 

    def stack_pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


# test stack

# my_stack = Stack(4)
# my_stack.stack_push(5)
# my_stack.stack_push(10)
# my_stack.stack_push(2)
# my_stack.print_stck()

# print("----------------")
# my_stack.stack_pop()
# my_stack.print_stck()






### Queues ###

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next    

    def enqueue(self,value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:    
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp




my_queue = Queue(5)
my_queue.enqueue(10)  
my_queue.enqueue(2)    
my_queue.enqueue(7)
my_queue.print_queue()              