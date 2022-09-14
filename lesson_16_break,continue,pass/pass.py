# about pass command

numbers = range(1,10)     #   -------------> 1,2,3,4,5,6,7,8,9



for number in numbers:
    if number%2==0:
        pass
    else:
        print(number)



# amma bu tek cut kodu rahat olaraq belede yazmaq olardi
numbers = range(1,10)     #   -------------> 1,2,3,4,5,6,7,8,9


# tek ededler ucun 
for number in numbers:
    if number%2!=0:
        print(number)

#cut edeler ucun 
for number in numbers:
    if number%2!=1:
        print(number)