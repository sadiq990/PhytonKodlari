##listden ilk herfin tapilmasi

#list = ['2', '1' , '3' '4']

#listin ilk herfini tapmaq istiyirkse matrisde oldugu kimi 0 1 2 3 bele sayima baslayiriq.

# print(list[0]) yazsaq console 2 gosterecek

# gorunduyu kimi 0 listdeki ilk reqemi printe verir.



list = ['2', '1' , '3' , '4']

search_number = '5'

if (search_number in list) and (search_number == list[0]):
    print("yes this letter on the list  and it is first number on the list")
elif search_number in list:
    print ("yes the number on the list but it is not first")
else:
    list.append(search_number)
    print("list has been uptaded")
    print ('updated list {}'.format(list) )
