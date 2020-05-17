
def validate(goals):

    try:
        int(goals)
        return True

    except:
        return False


def matchresult (teama, teamb, goalsa, goalsb):

    goalsa = int(goalsa)
    goalsb = int(goalsb)

    if(goalsa == goalsb):
        print("Empate!")
    
    elif(goalsa > goalsb):
        print("Vitória de: ", teama)
    
    elif(goalsb > goalsa):
        print("Vitória de: ", teamb)