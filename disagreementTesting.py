#DISAGREEMENT ALGORITHM TESTING

#number of disagreements
pluralityCondorcet = 0
pluralityBorda = 0
pluralityIRV = 0
condorcetBorda = 0
condorcetIRV = 0
bordaIRV = 0

#dictionaries of results
result1 = {'plurality': 'A', 'condorcet': 'C', 'borda': 'B', 'IRV': 'A'}
result2 = {'plurality': 'B', 'condorcet': 'B', 'borda': 'B', 'IRV': 'B'}
result3 = {'plurality': 'B', 'condorcet': 'A', 'borda': 'D', 'IRV': 'A'}
result4 = {'plurality': 'C', 'condorcet': 'C', 'borda': 'B', 'IRV': 'A'}
result5 = {'plurality': 'A', 'condorcet': 'C', 'borda': 'B', 'IRV': 'A'}

resultsArr = [result1, result2, result3, result4, result5]

numElections = len(resultsArr)

#loop through adding onto disagreement counts
for i in resultsArr:
    if i.get('plurality') != i.get('condorcet'):
        pluralityCondorcet += 1
    if i.get('plurality') != i.get('borda'):
        pluralityBorda += 1
    if i.get('plurality') != i.get('IRV'):
        pluralityIRV += 1
    if i.get('condorcet') != i.get('borda'):
        condorcetBorda += 1
    if i.get('condorcet') != i.get('IRV'):
        condorcetIRV += 1
    if i.get('borda') != i.get('IRV'):
        bordaIRV += 1

print(pluralityCondorcet, pluralityBorda, pluralityIRV, condorcetBorda, condorcetIRV, bordaIRV)

print("\nDisagreement percentages:\n")
print("Plurality-Condorcet: " + str((pluralityCondorcet/numElections) * 100) + "%")
print("Plurality-Borda: " + str((pluralityBorda/numElections) * 100) + "%")
print("Plurality-IRV: " + str((pluralityIRV/numElections) * 100) + "%")
print("Condorcet-Borda: " + str((condorcetBorda/numElections) * 100) + "%")
print("Condorcet-IRV: " + str((condorcetIRV/numElections) * 100) + "%")
print("Borda-IRV: " + str((bordaIRV/numElections) * 100) + "%")