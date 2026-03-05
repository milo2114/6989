import os 
from saludo import saludo
from despedida import despedida

def clear():
    os.system("cls")

def menu():
    options= input ("1. saludo\n2. ask for childe\n3. farewell\n4. Exit\nEnter your choice: ")
    if options == "1":
        saludo()    
    elif options == "2":
        print ("how are you my horse?")
    elif options == "3":
        print ("farewell my horse!")
    elif options == "4":
        despedida()
        menu() 
    else:       
        print ("invalid option")
        clear()
        menu()

if __name__ == "__main__":
    menu()
    print ("goodbye my laif")  


