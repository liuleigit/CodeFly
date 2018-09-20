# encoding=utf-8
# vim: set expandtab ts=4 sw=4 sts=4 tw=100
# python3

import os
import sys

class Singleton(type):
    """
    Singleton metaclass.
    __new__, __init__ will be exec for once.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class SingletonWithInit(type):
    """
    Singleton metaclass.
    __new__ will be exec for once.
    __init__ will be exec for every time of instanlizing.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonWithInit, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)

        return cls._instances[cls]

def test_Singleton():
    """
    class Singleton
    """
    class MyClass(metaclass=Singleton):
        def __new__(cls, *args, **kw):
            print("__new__")
            _instance = super(MyClass, cls).__new__(cls)
            _instance.x = 10
            _instance.i = 0
            _instance.l = []
            return _instance

        def __init__(self, ttt):
            print("__init__")
            self.i += 1
            self.l.append(ttt)

    l_1 = MyClass(111)
    print(l_1.x)
    print(l_1.i)
    print(l_1.l)

    l_2 = MyClass(999)
    print(l_1.x)
    print(l_1.i)
    print(l_1.l)

def test_SingletonWithInit():
    """
    class SingletonWithInit
    """
    class MyClass(metaclass=SingletonWithInit):
        def __new__(cls, *args, **kw):
            print("__new__")
            _instance = super(MyClass, cls).__new__(cls)
            _instance.x = 10
            _instance.i = 0
            _instance.l = []
            return _instance

        def __init__(self, ttt):
            print("__init__")
            self.i += 1
            self.l.append(ttt)

    l_1 = MyClass(111)
    print(l_1.x)
    print(l_1.i)
    print(l_1.l)

    l_2 = MyClass(999)
    print(l_1.x)
    print(l_1.i)
    print(l_1.l)

if __name__ == "__main__":
    test_Singleton()
    test_SingletonWithInit()
