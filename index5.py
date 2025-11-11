# Декоратор добавляют функциональность в существующий код
# Декоратор - это паттерн программирования, который позволяет добавлять НОВЫЙ ФУНКЦИОНАЛ к существующей функции

def gre():
    print("Привет")

hello = gre # Присваиваем функцию gre переменной hello
hello() # вызываем функцию gre через переменную hello 

# nnnnnn

def gromko(text):
    return text.upper()

def tiho(text):
    return text.lower()

def speak(func):
    messege= func("Hello ПКС -01 -25!")
    print(messege)

speak(gromko)
speak(tiho)
########



def inc(x):
    return x*2

def dec(x):
    return x/2

def oper(func, x):
    res = func(x)
    return res

print(oper(inc, 3))
print(oper(dec, 4))


####


def before_after(func):
    def wrapper():
        print("перед вызовом функции")
        func()
        print("после вызова") 

def sayHey():
    print("Привет друг!")
    

sayHey()

# №№№№№№№№№№№№№№№№
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        res = func(*args, **kwargs)
        print(f"Функция {func.__name__} вернула {res}")
        return res
    return wrapper

@logger
def add(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

add(4, 5, 6, 7, 8,)
add(56,77,n = 5, g = 7)
add(n = 5, g = 7)


# @property - это встроенный декоратор 
#     getter - получение
#     setter - изменение 
#     dteletter - удаление
#  Позволяет нам обращаться к методу как к полю атрибута

# без @property
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def get_area(self):
        return 3.14 * self.radius ** 2
    
c = Circle(5)
print(c.get_area)
##########
class Person:
    def __init__(self, name,):
        self.name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        print('сеттер сработал')
        if not isinstance(value, str):
            raise ValueError("Имя должно быть строкой")
        self.__name = value

    @name.deleter
    def name(self):
        print("Делеттер сработал")
        del self.__name

p = Person("Gena")
p.name = "Ivan"
print(p.name)
