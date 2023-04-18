from os import listdir
from time import sleep
import modules.votingMethods.plurality as plurality
import modules.votingMethods.condorcet as condorcet
import modules.votingMethods.borda as borda
import modules.votingMethods.irv as irv
import modules.generator.generateBallots as generator
import modules.disagreement as disagreement
import modules.tableCreator as tableCreator

#read votes function - returns array containing each ballot
def readVotes(f):
    lines = f.read().splitlines()
    votes = []

    for ballot in lines:
        votes.append(ballot.split(" "))

    return(votes)

#menu option 1 - generate ballot files and show disagreement table
def optionOne(numberOfCands, numberOfBallots):
    print("PLEASE WAIT - this may take a while, depending on your system")
    cands = generator.generateBallots(numberOfCands)
    
    generatedPath = './generator/ballotFiles'
    
    files = listdir(generatedPath)
    
    resultsArr = []

    for f in files:
        ballotFile = open(generatedPath + '/' + f)
        votes = readVotes(ballotFile)

        #error checking
        for ballot in votes:
            if len(ballot) != numberOfCands:
                print("Error: a ballot has been detected that does not have the number of candidates required - this may be due to user changes."
                            + "\n\nYou will be taken back to the main menu\n")
                sleep(2)
                menu()
            for cand in ballot:
                if cand not in cands:
                    print("Error: a candidate has been detected that is not part of the candidates list for this set of generated data."
                          + "\n\nYou will be taken back to the main menu\n")
                    sleep(2)
                    menu()
        if len(votes) != numberOfBallots:
            print("Error: the number of ballots detected is different from the number of ballots requested - this may be due to user changes."
                          + "\n\nYou will be taken back to the main menu\n")
            sleep(2)
            menu()

        
        pluralityResult = plurality.plurality(votes)
        condorcetResult = condorcet.condorcet(votes)
        bordaResult = borda.borda(votes)
        irvResult = irv.irv(votes)

        results = {'plurality': pluralityResult, 'condorcet': condorcetResult, 'borda': bordaResult, 'irv': irvResult}
        resultsArr.append(results)
    
    disagreementValues = disagreement.calculateDisagreement(resultsArr)

    tableCreator.createTable(disagreementValues)
    menu()

#menu option 2 - user select an existing ballot file and election results displayed
def optionTwo(f, numberOfCands, cands, numberOfBallots):
    
    #check that file exists
    try:
        ballotFile = open(f)
        votes = readVotes(ballotFile)

        #error checking
        for ballot in votes:
            if len(ballot) != numberOfCands:
                print("Error: a ballot has been detected that does not have the number of candidates required - this may be due to user changes."
                                + "\n\nYou will be taken back to the main menu\n")
                sleep(4)
                menu()
            for cand in ballot:
                if cand not in cands:
                    print("Error: a candidate has been detected that is not part of the candidates list for this set of generated data."
                            + "\n\nYou will be taken back to the main menu\n")
                    sleep(2)
                    menu()
        if len(votes) != numberOfBallots:
            print("Error: the number of ballots detected is different from the number of ballots requested - this may be due to user changes."
                            + "\n\nYou will be taken back to the main menu\n")
            sleep(2)
            menu()

        print("\nELECTION RESULTS FOR:\n")
        print("Plurality winner: " + plurality.plurality(votes))
        print("\nBorda count winner: " + borda.borda(votes))
        if condorcet.condorcet(votes) == '':
            print("\nCondorcet winner: NO CONDORCET WINNER")
        else:
            print("\nCondorcet winner: " + condorcet.condorcet(votes))
        print("\nIRV winner: " + irv.irv(votes) + "\n")
        menu()
    except FileNotFoundError:
        print("Error: file does not exist in the current directory. Could this have been a typo?"
              + "\n\nYou will be taken back to the main menu\n")
        sleep(2)
        menu()

#display menu
def menu():
    print("Menu:\n1. Generate ballot files - generate disagreement table\n2. Choose an existing ballot file - display voting method results of a single election\n3. Exit")
    menuChoice = int(input("> "))
    
    if menuChoice == 1:
        numCands = int(input("How many candidates per ballot would you like?: "))
        numBallots = int(input("How many ballots per election data file would you like?: "))
        optionOne(numCands, numBallots)
    
    elif menuChoice == 2:
        fileName = input("Enter the file name for which you would like to get election results for: ")
        numCands = int(input("How many candidates per ballot are there in the data file?: "))
        candidates = []
        for i in range(numCands):
            cand = input("Enter candidate " + str(i+1) + ": ")
            candidates.append(cand)
        numBallots = int(input("How many ballots are there in the data file?: "))
        optionTwo(fileName, numCands, candidates, numBallots)
    
    elif menuChoice == 3:
        exit()
    
    else:
        print("Invalid menu choice")
        menu()

#program title
def initialDisplay():
    print("__      __   _   _                _____ _                 _       _             ")
    sleep(0.05)
    print("\ \    / /  | | (_)              / ____(_)               | |     | |            ")
    sleep(0.05)
    print(" \ \  / /__ | |_ _ _ __   __ _  | (___  _ _ __ ___  _   _| | __ _| |_ ___  _ __ ")
    sleep(0.05)
    print("  \ \/ / _ \| __| | '_ \ / _` |  \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|")
    sleep(0.05)
    print("   \  / (_) | |_| | | | | (_| |  ____) | | | | | | | |_| | | (_| | || (_) | |   ")
    sleep(0.05)
    print("    \/ \___/ \__|_|_| |_|\__, | |_____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   ")
    sleep(0.05)
    print("                          __/ |                                                 ")
    sleep(0.05)
    print("                         |___/                                                  ")
    sleep(0.05)
    menu()

#initial function call
initialDisplay()