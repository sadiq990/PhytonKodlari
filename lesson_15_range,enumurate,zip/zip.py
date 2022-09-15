# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, 
# and then the second item in each passed iterator are paired together etc.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

#iterator1, iterator2, iterator3 ...	Iterator objects that will be joined together


a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

for names in zip(a,b):
    print(names)

#print result : 

# ('John', 'Jenny')
# ('Charles', 'Christy')
# ('Mike', 'Monica')

# Also we can use zip and range together but length of each itarable must be same

#for example: 

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
c = range(1,4)
for names in zip(c,a,b):
    print(names)


#Print result:
# (1, 'John', 'Jenny')
# (2, 'Charles', 'Christy')
# (3, 'Mike', 'Monica')

# we can also use enumurate 

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
for index,names in enumerate(zip(a,b)):
    print(index+1,names)

#Print result:
# 1 ('John', 'Jenny')
# 2 ('Charles', 'Christy')
# 3 ('Mike', 'Monica')

#you can use a len command to get information about the length of list

b = ("Jenny", "Christy", "Monica", "Vicky")
print(len(b))
# Print result: 4

