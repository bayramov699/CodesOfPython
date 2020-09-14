#dictionary
my_dict = {
    'name': 'Rauf',
    'surname': 'Bayramov',
    'age': '30',
    'city': 'Barda'
}
print(my_dict)
print(my_dict['city'])

#update a value of key in dictionary
my_dict['city'] = 'Baku'
print(my_dict)

#add a new key and value
my_dict['profession'] = 'programmer'
print(my_dict)

#remove a wrong addition
my_dict['key'] = 'value'
print(my_dict)
print(my_dict.pop('key'))
print(my_dict)
del my_dict['profession']
print(my_dict)

#for loop
for item in my_dict:
    print(item)

#the cube of the number
cube = {x: x*x*x for x in range(15)}
print(cube)
print(5 in cube)
print(16 in cube)
print(20 not in cube)

for i in cube:
    print(cube[i])

print(len(cube))

mix = {5, 1, 25, 18, 15}
print(sorted(mix))