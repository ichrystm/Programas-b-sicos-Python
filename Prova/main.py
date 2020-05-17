
import calculator

def menu():

    print(" ")
    a = input("Insira a pontuação obtida na prova: ")
    if calculator.validate(a):
        print(" ")
        calculator.calculator(a)
    else:
        print(" ")
        print("Valor inválido")

while True:
    menu()