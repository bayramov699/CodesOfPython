""" Object Oriented Programming """

class Person:
    def __init__(self, name, surname, person_type):
        self.name=name
        self.surname=surname
        self.person_type=person_type
        
    def __str__(self):
        return self.value
        
class Alive:
    def greeting(self):
        return f"Hello, Dear {self.name}. Welcome to my new program"
    
class Family(Person, Alive):
    pass
    
class Friend(Person, Alive):
    pass

class Collegue(Person, Alive):
    pass


address_book = {
    'family' : [],
    'friends' : [],
    'collegues':[]
}

name = input("Please, enter your name:")
surname = input("Please, enter your surname now:")
person_type = input("Please, enter person type(1-family, 2-friend, 3-collegue):")

if person_type=='1':
    prs=Family(name = name, surname = surname, person_type='family')
    address_book['family'].append(prs.__dict__)
elif person_type=='2':
    prs=Friend(name = name, surname = surname, person_type='friend')
    address_book['friends'].append(vars(prs))
elif person_type=='3':
    prs=Collegue(name = name, surname = surname, person_type='collegue')
    address_book['collegues'].append(vars(prs))

rauf= Family(name='Rauf', surname='Bayramov', person_type='family')

#print(Person.greeting())
print(address_book)
print(Family.greeting(rauf))
print(issubclass(Family, list))
print(isinstance(Family, tuple))
print(Friend.__mro__)
print(Friend.mro())