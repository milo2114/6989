import os 
def clear():
    os.system("cls")

def menu():
    options= input ("1. saludo\n2. ask for childe\n3. farewell\n4. Exit\nEnter your choice: ")
    if options == "1":
        print ("hellou my horse")
    elif options == "2":
        print ("how are you my horse?")
    elif options == "3":
        print ("farewell my horse!")
    elif options == "4":
        print ("good bye my horse!")
        clear()
        menu() 
    else:       
        print ("invalid option")
        clear()
menu()
print ("good bye my horse!")