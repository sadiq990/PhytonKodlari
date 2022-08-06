#zip iki eyni sayda olan  itirable i bir birine zipliyir:

countries = ['TR','US','UK','AZE','RU',]
siralamalar = range(1,4)

for country in zip(countries,siralamalar):
    print(country)