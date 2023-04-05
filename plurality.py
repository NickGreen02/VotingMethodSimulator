#read votes function - returns array containing each ballot
def readVotes(f):
    lines = f.read().splitlines()
    votes = []

    for ballot in lines:
        votes.append(ballot.split(" "))

    return(votes)




#print winners function - gets candidate with highest points from dictionary, prints winner
def printWinners(points):
    maxValue = max(points.values()) #get max value of points

    print("Winner(s):")
    for i in points:
        if points.get(i) == maxValue:
            print("Candidate " + i) #if candidate points value is winning value, print winning candidate




#plurality function - increments points dictionary based on plurality election system
def plurality(ballots):
    points = {} #initialise points dictionary
    for ballot in ballots:
        for cand in ballot:
            if cand not in points.keys():
                if ballot.index(cand) == 0:
                    points.update({cand: 1})    #if candidate key not in dictionary, add candidate
            else:
                if ballot.index(cand) == 0:
                    points[cand] = points[cand] + 1 #increment candidate value
    printWinners(points)




#main method
def main():
    ballotFile = open("ballots.txt")
    votes = readVotes(ballotFile)
    plurality(votes)
    ballotFile.close()

main()