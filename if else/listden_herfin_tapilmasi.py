## find any letter from list

list = ['a', 'b', 'c', 'd']

search_letter = 'e'

if search_letter in list:
    print("yes this letter on the list")
else:
    list.append(search_letter)
    print("list has been uptaded")
    print ('updated list {}'.format(list) )
    print ('{}' .format(list))