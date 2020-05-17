
def validate(a):

    try:
        float(a)
        return True

    except:
        return False

def calculator(a):

    a = float(a)

    if a <= 30:
        print("Regular")
    
    elif (a >= 31) and (a <=60):
        print("Bom")
    
    elif (a >= 61) and (a <= 90):
        print("Muito bom")
    
    elif (a >= 91) and (a <= 100):
        print("Ótimo")

    else:
        print("Pontuação inválida")