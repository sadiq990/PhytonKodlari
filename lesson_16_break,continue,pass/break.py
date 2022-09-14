#this is about break
# break 

Names = ('A' , 'B', 'C' , 'D', 'E' , 'V') * 20

for index, name in enumerate(Names):
    index += 1
    if name == 'B':
         print('Daxil etdiyiniz {} herfi {} dədir' .format(name,index))
         break
   
