
import calculator

def menu():

    print(" ")

    salario = input("Insira o valor total de seu salário: ")
    print("")

    if calculator.validate(salario):
        gastos = input("Insira o valor total de seus gastos: ")
        print("")

        if calculator.validate(gastos):
            calculator.calculasalario(salario, gastos)
        else:
            print("Valor inválido.")
    
    else:
        print("Valor inválido.")

while True:
    menu()



    




