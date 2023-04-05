import time

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
    print("Winner(s):")
    for i in points:
        if points.get(i) == maxValue:
            maxValCount += 1
    
    #if one winning candidate, iterate through dictionary printing the winner
    if maxValCount == 1:
        for c in points:
            if (points.get(c) == maxValue) and (points.get("tie"+c) == 0):  #check that candidate points equal max points value and has no ties
                print("Candidate " + c)
    else:
        print("No winner")

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

def menu():
    print("__      __   _   _                _____ _                 _       _             ")
    time.sleep(0.05)
    print("\ \    / /  | | (_)              / ____(_)               | |     | |            ")
    time.sleep(0.05)
    print(" \ \  / /__ | |_ _ _ __   __ _  | (___  _ _ __ ___  _   _| | __ _| |_ ___  _ __ ")
    time.sleep(0.05)
    print("  \ \/ / _ \| __| | '_ \ / _` |  \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|")
    time.sleep(0.05)
    print("   \  / (_) | |_| | | | | (_| |  ____) | | | | | | | |_| | | (_| | || (_) | |   ")
    time.sleep(0.05)
    print("    \/ \___/ \__|_|_| |_|\__, | |_____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   ")
    time.sleep(0.05)
    print("                          __/ |                                                 ")
    time.sleep(0.05)
    print("                         |___/                                                  ")
    time.sleep(0.05)

    print("DEMO VERSION\n")
    print("Menu:\n1. Run all four voting methods on ballots.txt\n2. Exit")
    menuChoice = int(input("> "))
    if menuChoice == 1:
        ballotFile = open("ballots.txt")
        votes = readVotes(ballotFile)
        print("Plurality:\n")
        plurality(votes)
        print("\nBorda count:\n")
        borda(votes)
        print("\nCondorcet:\n")
        condorcet(votes)
        print("\nIRV:\n")
        irv(votes)
    else:
        exit()

def main():
    menu()

main()