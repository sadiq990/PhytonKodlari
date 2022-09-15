# Phyton enumurate
## enumurate is for ordering lists.
#forexample:

letter_list = ['a','b','c','d','e']

for letter in letter_list:
    print(letter) 
# print result: a b c d e

#now we are going to use enumurate for ordering.

for  letter in enumerate(letter_list):
    print(letter) 


# print result
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')


# but with index we can use normal order 
for  index,letter in enumerate(letter_list):
    print(index,letter) 

#print result: 
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e

for  index,letter in enumerate(letter_list):
    print(index+1,letter) 

#print result: 
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e