
def validate(value):
    try:
        float(value)
        return True
    except:
        return False

def averagecalc(a, b, c):

    a = float(a)
    b = float(b)
    c = float(c)

    sum = a + b + c
    result = sum / 3

    if result >= 7:
        print("Aprovado!")

    else:
        print("Necesário inserir a nota da recuperação: ")
        rec = input("Digite a nota da recuperação: ")
        rec = float(rec)

        if rec >= 5:
            print("Aprovado na recuperação!")
        else:
            print("Reprovado!")