#range by default 0 dan ikinci verdiyimiz edede kimi ardicilqnan reqemleri verir :
Sayilar = list(range(10))
print(Sayilar)
#biz burda birinci reqemi vermemisy deye, by default 0 dan 10 a kimi reqemleri cixarir


#eger reqem veririkse onda:
Sayilar = list(range(2,10))
print(Sayilar)
# o zaman , 2den 9 a kimi olan reqemler cixir

# biz hettda 3 cu reqemide vere bilerik bu zaman 

Sayilar = list(range(2,20,2))
print(Sayilar)

# netice: [2, 4, 6, 8] kimi cixacaq

# rangei for ilede islede bilerik:

for randomnumbers in Sayilar:
    if randomnumbers> 5:
        print(randomnumbers)  #sayilar(2,20,2) range ile verilib  #netice : 6,8,10,12,14,16,18 
    

