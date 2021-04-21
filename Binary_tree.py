# each node will have at most 2 child nodes
# right child node will be larger than parent and left will be smaller

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_tree():
    def __init__(self):
        self.root = None
        self.space = 10

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.__insert(self.root, value)
    
    def __insert(self, curr, value):
        if value > curr.value:
            if curr.right == None:
                curr.right =  Node(value)
            else:
                self.__insert(curr.right, value)
        elif value < curr.value:
            if curr.left ==  None:
                curr.left = Node(value)
            else:
                self.__insert(curr.left, value)
        else:
            print(f'Value {value} is already in tree')

    def print_tree(self):
        if self.root == None:
            print("Empty tree")
        else:
            self.__print_tree(self.root,0)

        
    def __print_tree(self, curr, space):
        if curr == None:
            return
        space += self.space
        self.__print_tree(curr.right, space)

        print()
        for _ in range(space):
            print(end=' ')
        print(curr.value)

        self.__print_tree(curr.left,space)

    def get_height(self):
        if self.root==None:
            print('Empty tree')
        else:
            print(f'Tree height: {self.__get_height(self.root,0)}')

    def __get_height(self, curr, curr_height):
        if curr == None:
            return curr_height
        right_height = self.__get_height(curr.right, curr_height+1)
        left_height = self.__get_height(curr.left, curr_height+1)
        return max(right_height, left_height)
    
    def search(self, value):
        if self.root != None:
            return self.__search(value, self.root)
        else:
            return False
    
    def __search(self, value, curr):
        if curr.value == value:
            return True
        elif value > curr.value and curr.right !=None:
            return self.__search(value, curr.right)
        elif value < curr.value and curr.left !=None:
            return self.__search(value, curr.left)
        else:
            return False

def fill_tree(tree, num_ele = 20):
    from random import randint
    for _ in range(num_ele):
        tree.insert(randint(0,50))
    return tree

if __name__ == '__main__':
    tree = Binary_tree()
    fill_tree(tree)
    tree.print_tree()
    tree.get_height()

    tree2 = Binary_tree()
    tree2.insert(5)
    tree2.insert(1)
    tree2.insert(6)
    tree2.insert(2)
    tree2.insert(3)
    tree2.insert(10)
    tree2.insert(14)
    tree2.insert(4)
    tree2.insert(12)
    tree2.print_tree()
    tree2.get_height()
    value = 11
    if tree2.search(value):
        print(f'Value: {value} exist in tree')
