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




#process ballot function - assign points from ballots based on ranking
def processBallot(points, ballot):
    ballotRev = ballot[::-1]    #reverse order of ballot, so highest ranked candidate is last
    for cand in ballotRev:
        points[cand] = points[cand] + (ballotRev.index(cand))   #assign points value based on index




#borda function - initialises dictionary and calls helper function to assign points
def borda(ballots):
    points = {}

    #set all candidate points to 0
    startBal = ballots[0]
    for cand in startBal:
        points.update({cand: 0})
    
    #process each ballot
    for ballot in ballots:
        processBallot(points, ballot)
    
    printWinners(points)




#main method
def main():
    ballotFile = open("ballots.txt")
    votes = readVotes(ballotFile)
    borda(votes)
    ballotFile.close()

main()