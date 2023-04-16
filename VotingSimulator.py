from os import listdir
from time import sleep
import plurality
import condorcet
import borda
import irv
import generator.generateBallots as generator
import disagreement
import tableCreator

#read votes function - returns array containing each ballot
def readVotes(f):
    lines = f.read().splitlines()
    votes = []

    for ballot in lines:
        votes.append(ballot.split(" "))

    return(votes)

#menu option 1 - generate ballot files and show disagreement table
def optionOne(num):
    generator.generateBallots(num)
    
    generatedPath = './generator/ballotFiles'
    
    files = listdir(generatedPath)
    
    resultsArr = []

    for f in files:
        ballotFile = open(generatedPath + '/' + f)
        votes = readVotes(ballotFile)
        
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
def optionTwo(f):
    ballotFile = open(f)
    votes = readVotes(ballotFile)
    print("ELECTION RESULTS FOR:\n\n\n")
    print("Plurality: ")
    plurality(votes)
    print("\nBorda count: ")
    borda(votes)
    print("\nCondorcet: ")
    condorcet(votes)
    print("\nIRV: ")
    irv(votes)
    menu()

#display menu
def menu():
    print("Menu:\n1. Generate ballot files - generate disagreement table\n2. Choose an existing ballot file - display voting method results of a single election\n3. Exit")
    menuChoice = int(input("> "))
    if menuChoice == 1:
        numCands = int(input("How many candidates per ballot would you like?: "))
        optionOne(numCands)
    elif menuChoice == 2:
        fileName = input("Enter the file name for which you would like to get election results for: ")
        optionTwo(fileName) 
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