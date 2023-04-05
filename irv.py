#read votes function - returns array containing each ballot
def readVotes(f):
    lines = f.read().splitlines()
    votes = []

    for ballot in lines:
        votes.append(ballot.split(" "))

    return(votes)




#get loser function - returns the candidate with lowest first choices
def getLoser(points):
    minValue = min(points.values())
    for c in points:
        if (points.get(c) == minValue):
            loser = c
    return(loser)




#remove loser function - removes losing candidate from all ballots
def removeLoser(ballots, loser):
    for ballot in ballots:
        ballot.remove(loser)
    return(ballots)




#irv function - calculates winner based on IRV election system
def irv(ballots):
    #check if a candidate has a majority - simple plurality style dictionary method
    majorityCheck = False
    numBallots = len(ballots)
    points = {}
    for ballot in ballots:
        for cand in ballot:
            if cand not in points.keys():
                if ballot.index(cand) == 0:
                    points.update({cand: 1})
            else:
                if ballot.index(cand) == 0:
                    points[cand] = points[cand] + 1
    for c in points:
        if points.get(c) > (numBallots/2):  #if majority, set flag var to true and print winner
            print("Winner:")
            print("Candidate " + c)
            majorityCheck = True
            break
        else:
            majorityCheck = False
    
    #if no candidate has a majority, remove loser,
    #and call IRV algorithm again with new ballots
    if majorityCheck == False:
        loser = getLoser(points)
        newBallots = removeLoser(ballots, loser)
        irv(newBallots)





#main method
def main():
    ballotFile = open("ballots.txt")
    votes = readVotes(ballotFile)
    irv(votes)
    ballotFile.close()

main()