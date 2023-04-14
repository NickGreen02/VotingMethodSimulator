#print winners function - gets candidate with highest points from dictionary, prints winner
def printWinners(points):
    maxValue = max(points.values()) #get max value of points

    winString = ''
    for i in points:
        if points.get(i) == maxValue:
            winString += i #if candidate points value is winning value, print winning candidate

    return winString

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
    
    return printWinners(points)