#print winners function - gets candidate with highest points from dictionary, prints winner
def printWinners(points):
    maxValue = max(points.values()) #get max value of points

    for i in points:
        if points.get(i) == maxValue:
            return(i) #if candidate points value is winning value, print winning candidate

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
    return(printWinners(points))