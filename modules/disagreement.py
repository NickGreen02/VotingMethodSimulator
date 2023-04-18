def calculateDisagreement(resultsArray):
    numElections = len(resultsArray)
    
    #number of disagreements
    pluralityCondorcet = 0
    pluralityBorda = 0
    pluralityIRV = 0
    condorcetBorda = 0
    condorcetIRV = 0
    bordaIRV = 0

    #for loop to increment each disagreement value
    for i in resultsArray:
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

    #turn the disagreement integer values into disagreement percentages
    pCdisagreement = str(round(((pluralityCondorcet/numElections) * 100), 2))
    pBdisagreement = str(round(((pluralityBorda/numElections) * 100), 2))
    pIdisagreement = str(round(((pluralityIRV/numElections) * 100), 2))
    cBdisagreement = str(round(((condorcetBorda/numElections) * 100), 2))
    cIdisagreement = str(round(((condorcetIRV/numElections) * 100), 2))
    bIdisagreement = str(round(((bordaIRV/numElections) * 100), 2))

    #create array of disagreement percentages and return it, in the format the table creator program accepts
    disagreementArray = [[pCdisagreement, '', ''], [pBdisagreement, cBdisagreement, ''], [pIdisagreement, cIdisagreement, bIdisagreement]]
    return disagreementArray