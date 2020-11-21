class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Singly_Linked_list():
    def __init__(self):
        self.head = None
        self.len = 0

    def add(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = Node(val)
        self.len +=1

    def show(self):
        curr = self.head
        while curr != None:
            print(curr.val)
            curr = curr.next

    def remove(self, index):
        assert index <= self.len-1, "Index out of range!"
        if index == 0:
            self.head = self.head.next
        prev = self.head
        curr = self.head
        count = 0
        while count != index:
            prev = curr
            curr = curr.next
            count +=1
        prev.next = curr.next
        self.len -=1

    def reverse(self):
        if self.len == 0:
            return None
        elif self.len == 1:
            return self.head
        
        prev = None
        curr = self.head
        while curr != None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        self.head = prev

a = Singly_Linked_list()

from random import randint

for _ in range(10):
    a.add(randint(0,50))

a.show()
print()
a.remove(5)
a.show()
print()
a.reverse()
a.show()