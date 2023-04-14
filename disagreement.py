def calculateDisagreement(resultsArray):
    numElections = len(resultsArray)
    
    #number of disagreements
    pluralityCondorcet = 0
    pluralityBorda = 0
    pluralityIRV = 0
    condorcetBorda = 0
    condorcetIRV = 0
    bordaIRV = 0

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

    pCdisagreement = str((pluralityCondorcet/numElections) * 100) + "%"
    pBdisagreement = str((pluralityBorda/numElections) * 100) + "%"
    pIdisagreement = str((pluralityIRV/numElections) * 100) + "%"
    cBdisagreement = str((condorcetBorda/numElections) * 100) + "%"
    cIdisagreement = str((condorcetIRV/numElections) * 100) + "%"
    bIdisagreement = str((bordaIRV/numElections) * 100) + "%"

    disagreementArray = [[pCdisagreement, '', ''], [pBdisagreement, cBdisagreement, ''], [pIdisagreement, cIdisagreement, bIdisagreement]]

    return disagreementArray