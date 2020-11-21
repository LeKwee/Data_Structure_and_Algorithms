class Node():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class Binary_tree():
    def __init__(self):
        self.root = None
        self.space_step = 10

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self.__insert(val,self.root)

    def __insert(self, val, curr_node):
        if val < curr_node.val:
            if curr_node.left == None:
                curr_node.left = Node(val)
            else:
                self.__insert(val, curr_node.left)
        elif val > curr_node.val:
            if curr_node.right == None:
                curr_node.right = Node(val)
            else:
                self.__insert(val,curr_node.right) 
    
    def show(self):
        if self.root == None:
            return

        self.__show(self.root, 0)
        
    def __show(self, curr_node, space):
        if curr_node == None:
            return

        space += self.space_step
        self.__show(curr_node.right, space)

        print()
        for _ in range(space):
            print(end=" ")
        print (curr_node.val)

        self.__show(curr_node.left, space)
    
    def height(self):
        if self.root == None:
            return 0
        else:
            return self.__height(self.root, 0)
    
    def __height(self, curr_node, height):
        if curr_node == None:
            return height
        left_height = self.__height(curr_node.left, height+1)
        right_height = self.__height(curr_node.right, height+1)
        return max(left_height, right_height)

    def search(self, val):
        if self.root == None:
            return False
        else:
            return self.__search(self.root, val)

    def __search(self, curr_node, val):
        if curr_node== None:
            return False
        if curr_node.val == val:
            return True
        elif curr_node.val > val:
            return self.__search(curr_node.left, val)
        elif curr_node.val < val:
            return self.__search(curr_node.left, val)


tree = Binary_tree()
from random import randint
for _ in range(20):
    tree.insert(randint(5,50))

tree.show()
print(tree.height())
print(tree.search(22))
