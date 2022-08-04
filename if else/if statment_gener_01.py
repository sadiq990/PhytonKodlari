from lib2to3.pgen2.pgen import generate_grammar


gender_male= False
insani_keyfiyyet = True

if gender_male and insani_keyfiyyet:
    print("kisien sen ve yaxsi adamsan")
elif gender_male and not insani_keyfiyyet:
    print("kisisen sen amma pis adamsan")
else:
    print("qadinsen sen")
   
