""" Object Oriented Programming """

class Person:
    def __init__(self, name, surname, person_type):
        self.name=name
        self.surname=surname
        self.person_type=person_type
      

    def greeting(self):
        return f"Hello, Dear {self.name}. Welcome to my new program"

class Family(Person):
    pass
    
class Friend(Person):
    pass

class Collegue(Person):
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

#print(Person.greeting())
print(address_book)