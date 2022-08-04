first_number = float(input("ilk ededi daxil ediniz "))
oper = input (" enter operator ")
second_number = float(input(" ikinci ededi daxil ediniz "))

if oper == ("+"):
    print(first_number + second_number)
elif oper == ("-"):
    print(first_number - second_number)
elif oper == ("/"):
    print(first_number / second_number)
elif oper == ("*"):
    print(first_number * second_number)
else:
    print ("invalid operations")

