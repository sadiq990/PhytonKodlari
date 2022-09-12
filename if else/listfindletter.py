## in this tutorial we have a list like list = ['a', 'b' , 'c' , 'd']
## we are going to search , do we have a "f" letter on the list if not print no this letter is not on the list
## then with "append" we can add letter "f" to the list

# we need 2 variable
letter_list = ['a', 'b' , 'c' , 'd']
target_letter = 'f'
#if in command
if target_letter in letter_list:
    print("yes letter f is in the list")
else:
    print("no your letter is not on the list")
    print("but with .append we can add letter f to the list")
    letter_list.append(target_letter)
    print("we have updated the list")
    print('updated list {}'.format(letter_list))
