#print winners function - gets candidate with highest points from dictionary, prints winner
def print_winners(points):
    #get max value of points
    max_value = max(points.values())

    for i in points:
        if points.get(i) == max_value:
            #if candidate points value is winning value, print winning candidate
            return i

#plurality function - increments points dictionary based on plurality election system
def plurality(ballots):
    #initialise points dictionary
    points = {}
    for ballot in ballots:
        for cand in ballot:
            if cand not in points.keys():
                if ballot.index(cand) == 0:
                    #if candidate key not in dictionary, add candidate
                    points.update({cand: 1})
            else:
                if ballot.index(cand) == 0:
                    #increment candidate value
                    points[cand] = points[cand] + 1
    return print_winners(points)
