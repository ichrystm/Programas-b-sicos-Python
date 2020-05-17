
import calculator

def menu():

    print("")
    print("Calcule seu reajuste salarial")
    print(" ")

    salary = input("Digite o valor total do seu salário: ")

    if (calculator.validate(salary)):
        calculator.calculate(salary)
        
    else:
        print(" ")
        print("Valor inválido")

while True:
    menu()
