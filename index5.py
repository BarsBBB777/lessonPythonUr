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