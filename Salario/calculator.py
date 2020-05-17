
def validate(value):
    try:
        float(value)
        return True
    except:
        return False

def calculasalario(a, b):

    if a >= b:
        print("Gastos dentro do orçamento!")

    else: print("Orçamento estourado!")
