from random import sample

def generateBallots(totalCandVariation):
    baseCandAsc = 65
    candAscArr = [65]
    candidates = []

    for i in range(1,totalCandVariation):
        candAscArr.append(baseCandAsc + i)
    
    for i in candAscArr:
        candidates.append(chr(i))
    
    for i in range(50):
        textString = ""
        for x in range(100):
            if x < 99:
                textString += (" ".join(sample(candidates, len(candidates))) + '\n')
            else:
                textString += (" ".join(sample(candidates, len(candidates))))
    
        file = open("./generatorTesting/ballot" + str(i) + ".txt", "w")
        file.write(textString)
        file.close()

def main():
    generateBallots(4)

main()