import os 
from saludo import saludo
from despedida import despedida
from trabajando import saludo_trabajando

def clear():
    os.system("cls")

def menu():
    options= input ("1. saludo\n2. ask for childe\n3. farewell\n4. working\n 5. Exist \n Enter your choice: ")
    if options == "1":
        saludo()    
    elif options == "2":
        print ("how are you my horse?")
    elif options == "3":
        print ("farewell my horse!")
    elif options == "4":
        saludo_trabajando()
    elif options == "5":
        despedida()
        menu()
    else:       
        print ("invalid option")
        clear()
        menu()

if __name__ == "__main__":
    menu()
    print ("goodbye my laif")  


