from os import listdir
import plurality
import condorcet
import borda
import irv

#read votes function - returns array containing each ballot
def readVotes(f):
    lines = f.read().splitlines()
    votes = []

    for ballot in lines:
        votes.append(ballot.split(" "))

    return(votes)

def main():
    generatedPath = './generator/ballotFiles'
    
    files = listdir(generatedPath)
    
    resultsArr = []

    for f in files:
        ballotFile = open(generatedPath + '/' + f)
        votes = readVotes(ballotFile)
        
        pluralityResult = plurality.plurality(votes)
        condorcetResult = condorcet.condorcet(votes)
        bordaResult = borda.borda(votes)
        irvResult = irv.irv(votes)

        results = {'plurality': pluralityResult, 'condorcet': condorcetResult, 'borda': bordaResult, 'irv': irvResult}
        resultsArr.append(results)
    
    numElections = len(resultsArr)
    
    #number of disagreements
    pluralityCondorcet = 0
    pluralityBorda = 0
    pluralityIRV = 0
    condorcetBorda = 0
    condorcetIRV = 0
    bordaIRV = 0

    for i in resultsArr:
        if i.get('plurality') != i.get('condorcet'):
            pluralityCondorcet += 1
        if i.get('plurality') != i.get('borda'):
            pluralityBorda += 1
        if i.get('plurality') != i.get('irv'):
            pluralityIRV += 1
        if i.get('condorcet') != i.get('borda'):
            condorcetBorda += 1
        if i.get('condorcet') != i.get('irv'):
            condorcetIRV += 1
        if i.get('borda') != i.get('irv'):
            bordaIRV += 1
    
    print(pluralityCondorcet, pluralityBorda, pluralityIRV, condorcetBorda, condorcetIRV, bordaIRV)

    print("\nDisagreement percentages:\n")
    print("Plurality-Condorcet: " + str((pluralityCondorcet/numElections) * 100) + "%")
    print("Plurality-Borda: " + str((pluralityBorda/numElections) * 100) + "%")
    print("Plurality-IRV: " + str((pluralityIRV/numElections) * 100) + "%")
    print("Condorcet-Borda: " + str((condorcetBorda/numElections) * 100) + "%")
    print("Condorcet-IRV: " + str((condorcetIRV/numElections) * 100) + "%")
    print("Borda-IRV: " + str((bordaIRV/numElections) * 100) + "%")



main()