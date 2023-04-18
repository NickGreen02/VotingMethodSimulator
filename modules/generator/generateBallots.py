from random import sample
from os import mkdir

def generateBallots(totalCandVariation):
    #make folder for ballot files unless it already exists
    try:
        mkdir('./generator/ballotFiles')
    except FileExistsError:
        print("ballots folder already exists")


    baseCandAsc = 65
    candAscArr = [65]
    candidates = []

    #add candidates to candidates array via ascii addition
    for i in range(1,totalCandVariation):
        candAscArr.append(baseCandAsc + i)
    for i in candAscArr:
        candidates.append(chr(i))
    
    #generate the ballot files and their ballots
    for i in range(10000):
        textString = ""
        for x in range(100):
            if x < 99:
                textString += (" ".join(sample(candidates, len(candidates))) + '\n')
            else:
                textString += (" ".join(sample(candidates, len(candidates))))
    
        file = open("./generator/ballotFiles/ballot" + str(i) + ".txt", "w")
        file.write(textString)
        file.close()
    
    #return the candidates array for logic checks in main program
    return candidates