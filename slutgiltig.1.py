#Laboration 4
#Erik Hellström, Eyasu Alemiye
#Version 2

from linkeqny import LinkedQ
from bintreefile import Bintreelabb4
svenska = Bintreelabb4()
gamla = Bintreelabb4()


#Använder koden från laboration 3 för att läsa in orden och lagra i ett binärt träd
with open("ordlista.txt", "r", encoding = "utf-8") as svenskfil:
#with open("egenord.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()              # Ett trebokstavsord per rad
        if ordet in svenska:           #om ordet redan finns i listan kommer det ej läggas till som dublett
            pass 
            
        else:
            svenska.put(ordet)
        print(ordet)



#frågar om start & slutord
def fråga_ord():
    första_ord = input("skriv det första ordet: ")
    sista_ord = input("skriv det andra ordet: ")
    return första_ord, sista_ord




#skapar en ordlista för gamla ord:
def makechildren(startord,q):
    första_byte = [c + startord[1:] for c in 'abcdefghijklmnopqrstvuwxyzåäö']
    andra_byte = [startord[0:1] + c + startord[2:3] for c in 'abcdefghijklmnopqrstvuwxyzåäö']
    tredje_byte = [startord[0:2] + c + startord[3:] for c in 'abcdefghijklmnopqrstvuwxyzåäö']
    totallista = första_byte + andra_byte + tredje_byte
    print(totallista)
    
    for ordet in totallista:
        if ordet in svenska:
            if ordet not in gamla:
                print(ordet)
                q.enqueue(ordet)
                gamla.put(ordet)
                

                


def hitta_väg(startord,slutord):
    q = LinkedQ()
    gamla.put(startord)
    makechildren(startord,q)
    
    
    while True:
        
            if q.isEmpty() == True:
                print("INGEN VÄG")
                break
            else:
                
                uttaget = q.dequeue() 
                makechildren(uttaget,q)
            
            
                if uttaget == slutord:
                    print("finns en väg")
                    break





#funktionsanrop
valda_ord = fråga_ord() #hämtar input från användaren som returneras och lagras i en variabel valda_ord
hitta_väg(valda_ord[0],valda_ord[1]) #input tas som inparameter för att hitta väg mellan 2 st ord