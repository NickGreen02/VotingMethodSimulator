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
    ballotFile = open("ballots.txt")
    votes = readVotes(ballotFile)
    
    pluralityResult = plurality.plurality(votes)
    condorcetResult = condorcet.condorcet(votes)
    bordaResult = borda.borda(votes)
    irvResult = irv.irv(votes)

    results = {'plurality': pluralityResult, 'condorcet': condorcetResult, 'borda': bordaResult, 'irv': irvResult}
    print(results)

main()