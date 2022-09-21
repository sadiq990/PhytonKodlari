## map 

## quvvete yukseletmek :

from re import X


def quvvet(x):
    return x **2

print(quvvet(5))
 # print edende ekrana 25 cixacaq





eded = list(range(1,6))
print(eded)
for index in range(len(eded)):
    eded[index] = quvvet(eded[index])


print(eded)


## netice : 

# [1, 2, 3, 4, 5]
# [1, 4, 9, 16, 25]



 ## map ile bir ededi yox rangemizde olan ve ya listde olan butun edeleri istifade ede bilirik:
 # meselen:


def testmap():
    eded = list(range(3,6))
    return list(map(quvvet,eded))

print(testmap())



def cutreqemlerifitirle(x):
    if x%2 == 0:
        print("bu reqem cütdür")
        return x 
    else:
        print("bu reqem tekdir")
        return x
print(cutreqemlerifitirle(3))




## bu kodu bele de yazmaq olar 


def cutreqemlerifitirle2(x):
   print("cut eded") return x if x%2 == 0 else  None 

print(cutreqemlerifitirle2(3))