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
def read_votes(f):
    lines = f.read().splitlines()
    votes = []

    for ballot in lines:
        votes.append(ballot.split(" "))

    return(votes)

#menu option 1 - generate ballot files and show disagreement table
def option_one(number_of_cands, number_of_ballots):
    print("PLEASE WAIT - this may take a while, depending on your system")
    cands = generator.generate_ballots(number_of_cands, number_of_ballots)

    generated_path = './modules/generator/ballotFiles'

    files = listdir(generated_path)

    results_arr = []

    for f in files:
        ballot_file = open(generated_path + '/' + f)
        votes = read_votes(ballot_file)

        #error checking
        for ballot in votes:
            if len(ballot) != number_of_cands:
                print("Error: a ballot has been detected that does not have the number of " +
                    "candidates required - this may be due to user changes." +
                    "\n\nYou will be taken back to the main menu\n")
                sleep(2)
                menu()
            for cand in ballot:
                if cand not in cands:
                    print("Error: a candidate has been detected that is not part of the " +
                        "candidates list for this set of generated data." +
                        "\n\nYou will be taken back to the main menu\n")
                    sleep(2)
                    menu()
        if len(votes) != number_of_ballots:
            print("Error: the number of ballots detected is different from the " +
                "number of ballots requested - this may be due to user changes." +
                "\n\nYou will be taken back to the main menu\n")
            sleep(2)
            menu()


        plurality_result = plurality.plurality(votes)
        condorcet_result = condorcet.condorcet(votes)
        borda_result = borda.borda(votes)
        irv_result = irv.irv(votes)

        results = {'plurality': plurality_result, 'condorcet': condorcet_result,
                   'borda': borda_result, 'irv': irv_result}
        results_arr.append(results)

    disagreement_values = disagreement.calculate_disagreement(results_arr)

    tableCreator.create_table(disagreement_values)
    sleep(2)
    menu()

#menu option 2 - user selected folder and show disagreement table
def option_two(number_of_cands, cands, folder_path):
    try:
        print("PLEASE WAIT - this may take a while, depending on your system")
        files = listdir(folder_path)

        results_arr = []

        for f in files:
            ballot_file = open(folder_path + '/' + f)
            votes = read_votes(ballot_file)

            #error checking
            for ballot in votes:
                if len(ballot) != number_of_cands:
                    print("Error: a ballot has been detected that does not have the number of " +
                        "candidates required - this may be due to user changes." +
                        "\n\nYou will be taken back to the main menu\n")
                    sleep(2)
                    menu()
                for cand in ballot:
                    if cand not in cands:
                        print("Error: a candidate has been detected that is not part of the " +
                            "candidates list for this set of data." +
                            "\n\nYou will be taken back to the main menu\n")
                        sleep(2)
                        menu()


            plurality_result = plurality.plurality(votes)
            condorcet_result = condorcet.condorcet(votes)
            borda_result = borda.borda(votes)
            irv_result = irv.irv(votes)

            results = {'plurality': plurality_result, 'condorcet': condorcet_result,
                    'borda': borda_result, 'irv': irv_result}
            results_arr.append(results)

        disagreement_values = disagreement.calculate_disagreement(results_arr)

        tableCreator.create_table(disagreement_values)
        sleep(2)
        menu()
    except FileNotFoundError:
        print("\nFile path not found, sending you back to the main menu.")
        sleep(2)
        menu()

#menu option 3 - user select a single existing ballot file and election results displayed
def option_three(f, number_of_cands, cands, number_of_ballots):

    #check that file exists
    try:
        ballot_file = open(f)
        votes = read_votes(ballot_file)

        #error checking
        for ballot in votes:
            if len(ballot) != number_of_cands:
                print("Error: a ballot has been detected that does not have the number of " +
                    "candidates required - this may be due to user changes." +
                    "\n\nYou will be taken back to the main menu\n")
                sleep(2)
                menu()
            for cand in ballot:
                if cand not in cands:
                    print("Error: a candidate has been detected that is not part of the " +
                        "candidates list for this set of generated data." +
                        "\n\nYou will be taken back to the main menu\n")
                    sleep(2)
                    menu()
        if len(votes) != number_of_ballots:
            print("Error: the number of ballots detected is different from the " +
                "number of ballots requested - this may be due to user changes." +
                "\n\nYou will be taken back to the main menu\n")
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
        sleep(2)
        menu()
    except FileNotFoundError:
        print("Error: file does not exist in the current directory. Could this have been a typo?"
              + "\n\nYou will be taken back to the main menu\n")
        sleep(2)
        menu()

#display menu
def menu():
    print("Menu:\n1. Generate ballot files and generate a disagreement table" +
          "\n2. Select an existing folder of ballot files to generate a disagreement table for" +
          "\n3. Choose a single existing ballot file - display voting method results of a single election\n4. Exit")
    menu_choice = input("> ")

    if menu_choice == "1":
        try:
            num_cands = int(input("How many candidates per ballot would you like?: "))
            num_ballots = int(input("How many ballots per election data file would you like?: "))
            option_one(num_cands, num_ballots)
        except ValueError:
            print("\nInvalid input. Sending you back to main menu.")
            sleep(2)
            menu()

    elif menu_choice == "2":
        path = input("Enter the folder path you want to use (must be a relative path e.g. './testdata/ballotfiles'): ")
        try:
            num_cands = int(input("How many candidates per ballot are there?: "))
            candidates = []
            for i in range(num_cands):
                cand = input("Enter candidate " + str(i+1) + ": ")
                candidates.append(cand)
            option_two(num_cands, candidates, path)
        except ValueError:
            print("\nInvalid input. Sending you back to main menu.")
            sleep(2)
            menu()

    elif menu_choice == "3":
        file_name = input("Enter the path to the file for which you would like to get election results for " +
                          "(use a relative path if in another location e.g. './testdata/ballots.txt'): ")
        try:
            num_cands = int(input("How many candidates per ballot are there in the data file?: "))
            candidates = []
            for i in range(num_cands):
                cand = input("Enter candidate " + str(i+1) + ": ")
                candidates.append(cand)
            num_ballots = int(input("How many ballots are there in the data file?: "))
            option_three(file_name, num_cands, candidates, num_ballots)
        except ValueError:
            print("\nInvalid input. Sending you back to main menu.")
            sleep(2)
            menu()

    elif menu_choice == "4":
        exit()

    else:
        print("\nInvalid menu choice")
        sleep(2)
        menu()

#program title
def initial_display():
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
initial_display()
