# Bu kodda, listde olan ad ve soyad split ile ayrilacaq, ve ad soyad nomre ile duzulecek

employees = ["Sadig Musazade" , "Agsin Aligulov" , "Shamo Handamov"]
numbers = 0

for alllist in employees:
    numbers = numbers + 1
    name = alllist.split()[0]
    surname = alllist.split()[1]
    print('{0}.   Employee Name is {1} and his Surname {2}' .format(numbers, name, surname) )