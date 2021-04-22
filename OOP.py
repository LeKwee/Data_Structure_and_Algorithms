class parent():
    def __init__(self):
        self.public = 1
        self._protected = 2
        self.__private = 3
        
    def func1(self):
        print ('parent')

    def __private_func1(self):
        print('This is so private')

    def __repr__(self) -> str:
        return '__repr__'

class child1(parent):
    def func1(self):
        print('child1')

class child2(child1,parent):
    def func1(self):
        parent.func1(self)

c2 = child2()
p = parent()

# overrides func1() in child2 to call func1() in parent
c2.func1()

# calling private function from parent 
p._parent__private_func1()
c2._parent__private_func1()

# dunder functions are not private
print(p.__repr__())

print(p)
print(c2.public)
print(p.public)

# protected is just a naming convention with a single underscore
print(c2._protected)
print(p._protected)

print(c2._parent__private)
print(p.__private)

'''
OUTPUT:

parent
This is so private
This is so private
__repr__
__repr__
1
1
2
2
3
Traceback (most recent call last):
  File "OOP.py", line 46, in <module>
    print(p.__private)
AttributeError: 'parent' object has no attribute '__private'
'''