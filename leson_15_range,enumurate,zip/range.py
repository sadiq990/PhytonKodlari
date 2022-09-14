range_list = list(range(0,10))
print(range_list)

#printr result is : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

range_list = list(range(2,6))
print(range_list)

#printr result is [2, 3, 4, 5]


range_list = list(range(3,30,3)) 
print(range_list)

#print  result [3, 6, 9, 12, 15, 18, 21, 24, 27]

# we can also use range in for 
#for example 

range_list = range(1,11)
for numberlist in range_list:
    print(numberlist)

# print result : 1 2 3 4 5 6 7 8 9 10



for randomnumbers in range_list:
    if randomnumbers> 5:
        print(randomnumbers)