# -*- coding: utf-8 -*-
"""Singleton.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1irPw5ggAilWWwgH4BV-4GIKgwm-QEXO5
"""

'''
Singleton implementation 1
'''

class Singleton():
  __instance = None

  @staticmethod
  def getInstance():
    if Singleton.__instance == None:
      Singleton()
    return Singleton.__instance

  def __init__(self):
    if Singleton.__instance != None:
      raise Exception('Singleton already exist!')
    else:
      Singleton.__instance = self

s1 = Singleton.getInstance()
print(s1)
s2 = Singleton.getInstance()
print(s2)
s3 = Singleton()

# outputs
# <__main__.Singleton object at 0x7f2e19b2ba30>
# <__main__.Singleton object at 0x7f2e19b2ba30>
# Exception: Singleton already exist!

'''
Singleton implementation 2
'''

class Singleton():
  __instance = None

  def __new__(cls): #cls is a reference to the class itself, as good as typing Singleton
    if cls.__instance == None:
      cls.__instance = super(Singleton, cls).__new__(cls)

    return cls.__instance

s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)
s3 = Singleton()
print(s3)

# outputs
# <__main__.Singleton object at 0x7f2e19b7a200>
# <__main__.Singleton object at 0x7f2e19b7a200>
# <__main__.Singleton object at 0x7f2e19b7a200>

