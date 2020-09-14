#integer set
my_set = {1, 2, 3}
print(my_set)

#add item to set
my_set.add('hello world')
print(my_set)

#add item to set (divide into parts) 
my_set.update('python')
print(my_set)

#remove item from set(with error)
my_set.remove(1)
print(my_set)

#remove item from set(without error)
my_set.discard(1)
print(my_set)

#remove item with pop
my_set.pop()
print(my_set)

pop_item = my_set.pop()
print(pop_item)

#clear everything in set
my_set.clear()
print(my_set)


new_set1 = {'what', 'is', 'your', 'name', 'sir'}
new_set2 = {'my', 'name', 'is', 'Rauf', 'sir'}
#union of sets
print(new_set1 | new_set2)
print(new_set2 | new_set1)
print(new_set1.union(new_set2))
print(new_set2.union(new_set1))

#show which items exist in both sets
print(new_set1.intersection(new_set2))
print(new_set2.intersection(new_set1))
print(new_set1 & new_set2)
print(new_set2 & new_set1)

#show which items is different
print(new_set1.difference(new_set2))
print(new_set2.difference(new_set1))
print(new_set1 - new_set2)
print(new_set2 - new_set1)

#show which items is different in both sets
print(new_set1.symmetric_difference(new_set2))
print(new_set2.symmetric_difference(new_set1))
print(new_set1 ^ new_set2)
print(new_set2 ^ new_set1)

#add item to set
my_set.add('new_addition')
print(my_set)

#copy set to a new set
new_set3 = my_set.copy()
print(new_set3)

#for loop
for word in new_set1:
    print(word)

print(len(new_set1))
print(all(new_set1))
print(any(new_set1))
print(max(new_set1))
print(min(new_set1))
