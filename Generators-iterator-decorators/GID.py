#ITERATOR

my_list = [1,2,7]

my_iter = iter(my_list)

print(next(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())


#iterate with while loop
while True:
    try:
        element = next(my_iter)
    except StopIteration:
        break
    print(element)

class PowFour:
    ''' class for power of four '''
    def __init__(self, max=0):
        self.max=max
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 4**self.n
            self.n+=1
            return result
        else:
            raise StopIteration

for i in PowFour(5):
    print(i)

#GENERATOR

def my_gen():
    n = 15*5
    print("This is first print")
    yield n

    n=5*2
    print("This is second print")
    yield n

    n=10/2
    print("This is last print")
    yield n

for item in my_gen():
    print(item)


#DECORATOR

def sayHello(func):
    def inner():
       print("Hello, darling") 
       func()
    return inner

def AskAge():
    print("How old are you?")
new_func = sayHello(AskAge)

print(new_func())


def Dollar(func):
    def inner(*args, **kwargs):
        print("$"*10)
        func(**args, **kwargs)
        print("$"*10)
    return inner

@Dollar
def SayBye():
    print("Good Bye, Dears")

print(SayBye())