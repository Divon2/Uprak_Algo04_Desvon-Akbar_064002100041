def menu() :
   print("1.Desimal ke Binier")
   print("2.Binier ke Desimal") 
   print("Exit") 
   


desimal = int(input('Masukkan Bilangan Desimal = '))

biner = bin(desimal) .replace("","")
oktal = oct(desimal) .replace("","")
hexa = hex(desimal) .replace("","")
print(biner,oktal,hexa)

biner = input() 
desimal = 0
pangkat =len(biner)-1

for i in range(len(biner)) :
    idesimal = int(biner[i]) *2** pangkat
    desimal +=idesimal
    pangkat -=1
    print("Biniernya Adalah=",desimal) 
while desimal !=0:
    if desimal ==1:
        #do Desimal ke Binier
 elif desimal ==2:
 #do binier ke desimal
 else:
    print("selesai") 
            
            menu() 
            desimal= int(input("selesai")) 