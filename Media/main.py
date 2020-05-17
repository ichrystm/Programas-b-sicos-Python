
import calculator

def menu():

    a = input("Digite o valor da primeira nota: ")
    if calculator.validate(a):
        b = input("Digite o valor da segunda nota: ")
        if calculator.validate(b):
            c = input("Digite o valor da terceira nota: ")
            if calculator.validate(c):
                print(" ")
                calculator.averagecalc(a, b, c)
            else:
                print("Valor inválido.")
        else:
            print("Valor inválido.")
    else:
        print("Valor inválido.")

while True:
    menu()