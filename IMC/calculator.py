
def validate(value):
    
    try:
        float(value)
        return True

    except:
        pass
        return False

def imccalc(weight, height):

    weight = float(weight)
    height = float(height)

    height2 = height * height

    imc = weight / height2

    if(imc <= 18.5):
        print(" ")
        print("Magro")
    
    elif( (imc > 18.5) and (imc <= 25) ):
        print(" ")
        print("Normal")

    elif( (imc > 25) and (imc <= 30) ):
        print(" ")
        print("Sobrepeso")
    
    elif( imc > 30):
        print(" ")
        print("Obeso")
