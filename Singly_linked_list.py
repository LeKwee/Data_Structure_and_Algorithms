class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Linked_list():
    def __init__(self):
        self.head = Node()
        self.len = 0

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
        cur_node.next = new_node
        self.len += 1

    def display(self):
        items = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            items.append(cur_node.data)
        print(items)
    
    def getLen(self):
        print('Number of elements in linked-list: %d'% self.len)

    def erase(self, index):
        if index >= self.len:
            print('Erase index out of range')
            return
        
        count = 0
        cur_node = self.head
        
        while True:
            previous_node = cur_node
            cur_node=cur_node.next
            if count == index:
                previous_node.next = cur_node.next
                self.len-=1
                return
            count+=1

    def reverse(self):
        prev = None
        curr = self.head.next
        while (curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = Node()
        self.head.next = prev

    def getIndex(self, index):
        if index >= self.len:
            print('Get index out of range')
            return
        count = 0
        curr =  self.head
        while True:
            curr=curr.next
            if count == index:
                return curr.data
            count+=1
        

def test_append():
    linked_list = Linked_list()
    linked_list.append('a')
    assert linked_list.getIndex(0) == 'a', "Append index[0] failed"
    linked_list.append('b')
    assert linked_list.getIndex(1) == 'b', "Append index[0] failed"
    print("Test append succeeded!")

def test_erase():
    linked_list = Linked_list()
    linked_list.append('a')
    linked_list.append('b')
    linked_list.append('c')
    linked_list.append('d')
    linked_list.erase(1)
    assert linked_list.getIndex(1)=='c', f"Erase index one failed. Suppose to be 'c' but is {linked_list.getIndex(1)}"
    print("Test erase succeeded!")

def test_reverse(Llist):
    Llist.reverse()
    Llist.display()


if __name__ == "__main__":
    test_append()
    test_erase()

    linked_list = Linked_list()
    linked_list.append('a')
    linked_list.append('b')
    linked_list.append('c')
    linked_list.append('d')
    test_reverse(linked_list)