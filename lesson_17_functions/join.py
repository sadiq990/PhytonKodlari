## join is reverse of split.

"""

Join written like "  ".join([name,surname])

join iki iterasiyani birlesdirmek ucun istifade olunur.
splitin tam eksidir .

"""



def name_and_surname(name,surname):
   return "  ".join([name,surname])




print(name_and_surname("sadiq","musazade"))

#bu kodda problem odurki, name surname iki dir eger bir adamin adi 3 ayri sozden
#ibaretdirse onda kod error verecek ona gorede biz argsden istifade edirik.




#arg islenme qaydasi
def name_and_surname(*args):
   return "  ".join(args)

print(name_and_surname("Mirze","Elekber","Sabir"))


