
import comparator

def menu():

    print(" ")
    teama = input("Digite o nome do primeiro time: ")
    goalsa = input("Digite a quantidade de gols do primeiro time: ")

    if comparator.validate(goalsa):

        print(" ")
        teamb = input("Digite o nome do segundo time: ")
        goalsb = input("Digite a quantidade de gols do segundo time: ")

        if comparator.validate(goalsb):

            print(" ")
            comparator.matchresult(teama, teamb, goalsa, goalsb)
        
        else: 

            print(" ")
            print("Valor inválido.")
        
    else: 

        print(" ")
        print("Valor inválido.")

while True:
    menu()
