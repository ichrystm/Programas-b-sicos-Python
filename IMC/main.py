
import calculator

def menu():

    print(" ")
    print("Calculador de IMC")
    print(" ")

    weight = input("Insura seu peso (Em quilogramas): ")

    if(calculator.validate(weight)):

        height = input("Insura sua altura (Em metros): ")

        if(calculator.validate(height)):

            calculator.imccalc(weight, height)

        else:
            print(" ")
            print("Valor inválido")

    else: 
        print(" ")
        print("Valor inválido")

    
while True:
    menu()


