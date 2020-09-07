name = input('Please, enter your name:')
surname = input('Please, enter your surname:')
age = input('Please, enter your age:')

f = open("test.txt", "w")
f.write(f"{name} {surname} {age}")
f.close()

f = open("test.txt", "r")
print(f.read())