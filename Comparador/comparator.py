

def compare(a, b):

    if a == b:
        print(" ")
        print("Igualdade comprovada!")

    elif a < b:
        print(" ")
        print("Ordem crescente: ", b, " ", a )

    elif b < a:
        print(" ")
        print("Ordem crescente: ", a, " ", b)


def validate(number):

    try:
        float(number)
        return True

    except:
        pass
        return False







