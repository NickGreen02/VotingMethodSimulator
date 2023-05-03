from random import sample
from os import mkdir

def generate_ballots(total_cand_variation, num_ballots):
    #make folder for ballot files unless it already exists
    try:
        mkdir('./modules/generator/ballotFiles')
    except FileExistsError:
        print("Ballots folder detected - any existing files will be replaced.")


    base_cand_asc = 65
    cand_asc_arr = [65]
    candidates = []

    #add candidates to candidates array via ascii addition
    for i in range(1,total_cand_variation):
        cand_asc_arr.append(base_cand_asc + i)
    for i in cand_asc_arr:
        candidates.append(chr(i))

    #generate the ballot files and their ballots
    for i in range(10000):
        text_string = ""
        for x in range(num_ballots):
            if x < num_ballots - 1:
                text_string += (" ".join(sample(candidates, len(candidates))) + '\n')
            else:
                text_string += (" ".join(sample(candidates, len(candidates))))

        f = open("./modules/generator/ballotFiles/ballot" + str(i) + ".txt", "w")
        f.write(text_string)
        f.close()

    #return the candidates array for logic checks in main program
    return candidates
