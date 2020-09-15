from functools import reduce

#map function

def calculateCube(n):
    return n*n*n

ints = (1, 5, 18, 4, 13)

result = map(calculateCube, ints)

print(result)

numbersCube = set(result)
print(numbersCube)


#lambda function with lambda

nums = (5, 12, 24, 8, 36, 58)

result = map(lambda x: x*x+x, nums)

print(result)

main_result = set(result)

print(main_result)

#multiple iterators with lambda

nums_2 = (10, 22, 7, 18, 29, 35)

result = map(lambda x1, x2: x1+x2, nums, nums_2)
print(list(result))

#filter function

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numbers_2=(2, 4, 6, 8, 10)
def filterNumbers(numbers):
    if(numbers in numbers_2):
        return True
    else:
        return False
filteredNumbers = filter(filterNumbers, numbers)
for number in filteredNumbers:
    print(number)


#reduce function

def resultNumbers(a, b):
    return (a*b)+(a/b)

result = reduce(resultNumbers, [1,2,3,4])

print(result)


#zip function

cities = ['baku', 'ganja', 'barda', 'sumqayit', 'abseron', 'terter']

carSerialNumbers = ["10", "20", "09", "50", "01", "59"]

orderNumber = (1, 2, 3, 4, 5, 6)

result1 = zip(cities, carSerialNumbers)

result_list = list(result1)

print(result_list)

result2 = zip(orderNumber, cities, carSerialNumbers)

result_set = set(result2)

print(result_set)

a, b, c = zip(*result_set)

print('N=', a)
print('name of city=', b)
print('car serial number=', c)
