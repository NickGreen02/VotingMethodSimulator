#head-to-head function - simulates condorcet head to heads
def head2head(ballots, candidate1, candidate2):
    cand1total = 0
    cand2total = 0
    for ballot in ballots:
        #if candidate is higher ranked, increment points for that candidate
        if ballot.index(candidate1) < ballot.index(candidate2):
            cand1total += 1
        else:
            cand2total += 1
    if cand1total > cand2total:
        return candidate1
    if cand1total < cand2total:
        return candidate2
    if cand1total == cand2total:
        return "tie"

#condorcet function - initialises dictionary with candidates and tie values,
#loops through ballots calling head-to-head helper function
def condorcet(ballots):
    points = {}

    #set all candidate and tie points to 0
    startBal = ballots[0]
    for cand in startBal:
        points.update({cand: 0})
        points.update({"tie"+cand: 0})
    
    candidates = ballots[0]
    numPairs = 0
    for cand1 in candidates:
        for cand2 in candidates:
            if (cand2 != cand1) and (candidates.index(cand1) < candidates.index(cand2)):
                numPairs += 1
                winner = head2head(ballots, cand1, cand2)
                if winner != "tie":
                    points[winner] += 1 #if there is a winner in the head2head, increment winner points by 1
                else:   #otherwise, increment tie points for each candidate
                    points["tie"+cand1] += 1   
                    points["tie"+cand2] += 1
    
    #get max value of points from dictionary
    maxValue = max(points.values())
    maxValCount = 0

    #iterate through dictionary, checking that there is only one candidate who wins
    for i in points:
        if points.get(i) == maxValue:
            maxValCount += 1
    
    #if one winning candidate, iterate through dictionary printing the winner
    if maxValCount == 1:
        for c in points:
            if (points.get(c) == maxValue) and (points.get("tie"+c) == 0):  #check that candidate points equal max points value and has no ties
                return c
    else:
        return ''