#get loser function - returns the candidate with lowest first choices
def get_loser(points):
    min_value = min(points.values())
    for c in points:
        if (points.get(c) == min_value):
            loser = c
    return loser

#remove loser function - removes losing candidate from all ballots
def remove_loser(ballots, loser):
    for ballot in ballots:
        ballot.remove(loser)
    return ballots

#irv function - calculates winner based on IRV election system
def irv(ballots):
    #check if a candidate has a majority - simple plurality style dictionary method
    majority_check = False
    num_ballots = len(ballots)
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
        #if majority, set flag var to true and print winner
        if points.get(c) > (num_ballots/2):
            majority_check = True
            return c
        else:
            majority_check = False

    #if no candidate has a majority, remove loser,
    #and call IRV algorithm again with new ballots
    if majority_check == False:
        loser = get_loser(points)
        new_ballots = remove_loser(ballots, loser)
        return irv(new_ballots)
