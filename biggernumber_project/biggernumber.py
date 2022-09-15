##  we are going to add 3 number and code going to identify which one is biger.


def bignumber():
    print("you are going to add 3 number program going to identify which number is bigger")
    first_number = int(input("add first number "))
    second_number = int(input("add second number "))
    third_number = int(input("add third number "))
    print("you have entered {}, {}, {}".format(first_number,second_number,third_number))
    if first_number > second_number and first_number > third_number:
        print("big number is {}" .format(first_number))
    elif second_number > first_number and second_number > third_number:
         print("big number is {}" .format(second_number))
    else:
        print("big number is {}" .format(third_number))





        
print(bignumber())



