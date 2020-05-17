
def validate(value):
    
    try:
        float(value)
        return True

    except:
        pass
        return False


def calculate(salary):

    salary = float(salary)

    if salary <= 2000:
        salary = salary * 1.5
        print(" ")
        print("O reajuste é de 50%. Valor com reajuste: ", salary)
    
    elif (salary > 2000) and (salary < 5000):
        salary = salary * 1.2
        print(" ")
        print("O reajuste é de 20%. Valor com reajuste: ", salary)

    else: 
        salary = salary * 1.1
        print(" ")
        print("O reajuste é de 10%. Valor com reajuste: ", salary)
