# Bu kodda, listde olan ad ve soyad split ile ayrilacaq, ve ad soyad nomre ile duzulecek
# elave olaraq admin deyeri verilir, ve admin siyahida varsa admin username and surname cixir



admin = "Sadig Musazade"
employees = ["Sadig Musazade", "Agsin Aligulov" , "Shamo Handamov"]
#bu numbers ad soyadin reqemlenmesi ucun istifade olunan variable dir
numbers = 0
#bu admin_numbers admin  ad soyadin reqemlenmesi ucun istifade olunan variable dir
admin_numbers=0

for alllist in employees:
    # numbers = numbers + 1
    name = alllist.split()[0]
    surname = alllist.split()[1]
    # admin ad soyadi employees listinde varsa
    if ( alllist == admin):
    #    admin += 1 
       print('{0}. Admin name   {} Admin surname {}' .format(admin_numbers,name,surname) )
    else:
        # numbers +=1
        print('{0}.   Employee Name is {1} and his Surname {2}' .format(numbers, name, surname) )




  