#Laboration 4
#Erik Hellström, Eyasu Alemiye
#Version 1


#Läser in klassen för binära träd
from bintreefile import Bintreelabb4


#Använder koden från laboration 3 för att läsa in orden och lagra i ett binärt träd
svenska = Bintreelabb4()
with open("Laboration 4\ordlista.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()              # Ett trebokstavsord per rad
        if ordet in svenska:           #om ordet redan finns i listan kommer det ej läggas till som dublett
            pass 
            
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")




#frågar om start & slutord
def fråga_ord():
    första_ord = input("skriv det första ordet: ")
    sista_ord = input("skriv det andra ordet: ")
    return första_ord, sista_ord






#skapar en ordlista för gamla ord:
def makechildren(startord):
    gamla = Bintreelabb4()
    #barnlista = []
    första_byte = [c + startord[1:] for c in 'abcdefghijklmnopqrstvuwxyzåäö']
    andra_byte = [startord[0:1] + c + startord[2:3] for c in 'abcdefghijklmnopqrstvuwxyzåäö']
    tredje_byte = [startord[0:2] + c + startord[3:] for c in 'abcdefghijklmnopqrstvuwxyzåäö']
    totallista = första_byte + andra_byte + tredje_byte
    for ordet in totallista:
        if ordet in svenska:
            if ordet not in gamla:
                gamla.put(ordet)

                if ordet == startord:
                    pass

                else:
                    print(ordet)
                
            else:
                pass
      
        else:
            continue
            











valda_ord = fråga_ord()
makechildren(valda_ord[0])














































# #frågar efter startord och slutord, ordet som efterfrågas ska vara 3 bokstäver långt och finnas i ordlistan





# fråga_ord()