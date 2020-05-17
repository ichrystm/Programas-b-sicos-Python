
import comparator

def menu():

    print(" ") 
    a = input("Digite o primeiro número: ")

    if(comparator.validate(a)):
        print("")
        b = input("Digite o segundo número: ")
        if(comparator.validate(b)):
            comparator.compare(a, b)
        
        else:
            print("")
            print("Digite um número válido.")

    else: 
        print(" ")
        print("Digite um número válido.")

while True:
    menu()



