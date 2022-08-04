#

employees_list = ["Sadig Musazade", "Agsin Aligulov" , "Shamo Handamov", "MirSadiq Hesenli" , "Memmedov Behmen" ]
admin = "Memmedov Behmen"
name_numbers = 0
admin_numbers = 0



for names in employees_list:
    # name_numbers += 1
    Employee_name = names.split()[0]
    Employee_surname = names.split()[1]
    # print('{0}. Employee name: {1} Surname: {2}'.format(name_numbers,Employee_name,Employee_surname))\
    if (names == admin):
        admin_numbers = admin_numbers + 1
        print('{0}. Admin name: {1} Surname: {2}'.format(admin_numbers,Employee_name,Employee_surname))
    else:
         name_numbers += 1
         print('{0}. Employer name: {1} Surname: {2}'.format(name_numbers,Employee_name,Employee_surname))


    