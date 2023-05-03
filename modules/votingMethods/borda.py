#print winners function - gets candidate with highest points from dictionary, prints winner
def print_winners(points):
    #get max value of points
    max_value = max(points.values())

    win_string = ''
    for i in points:
        if points.get(i) == max_value:
            #if candidate points value is winning value, print winning candidate
            win_string += i

    return win_string

#process ballot function - assign points from ballots based on ranking
def process_ballot(points, ballot):
    #reverse order of ballot, so highest ranked candidate is last
    ballot_rev = ballot[::-1]
    for cand in ballot_rev:
        #assign points value based on index
        points[cand] = points[cand] + (ballot_rev.index(cand))

#borda function - initialises dictionary and calls helper function to assign points
def borda(ballots):
    points = {}

    #set all candidate points to 0
    start_bal = ballots[0]
    for cand in start_bal:
        points.update({cand: 0})

    #process each ballot
    for ballot in ballots:
        process_ballot(points, ballot)

    return print_winners(points)
