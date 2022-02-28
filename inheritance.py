class Parent():
    population =50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func1(self):
        print(self.name)
    
    def __repr__(self):
        return (self.name)

class Child1(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)

    def func1(self):
        print(self.name)

    @staticmethod
    def get_year_born(age):
        print(2021-age)

    @classmethod
    def get_population(cls):
        print(f'population: {cls.population}')
        
p = Parent('parent', 32)
c1 = Child1('child1', 12)

print(p)
print(c1) 

c1.get_year_born(c1.age)
Child1.get_population()

import time
def time_func(func):
    def wrapper(*args, **kargs):
        start = time.time()
        func(*args, **kargs)
        print(time.time() - start)

    return wrapper

@time_func
def add_sleep(param1,param2,param3):
    print(param1+param2+param3)
    time.sleep(2)


add_sleep(1,2,3)
