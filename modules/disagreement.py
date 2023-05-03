def calculate_disagreement(results_array):
    num_elections = len(results_array)

    #number of disagreements
    plurality_condorcet = 0
    plurality_borda = 0
    plurality_irv = 0
    condorcet_borda = 0
    condorcet_irv = 0
    borda_irv = 0

    #for loop to increment each disagreement value
    for i in results_array:
        if i.get('plurality') != i.get('condorcet'):
            plurality_condorcet += 1
        if i.get('plurality') != i.get('borda'):
            plurality_borda += 1
        if i.get('plurality') != i.get('irv'):
            plurality_irv += 1
        if i.get('condorcet') != i.get('borda'):
            condorcet_borda += 1
        if i.get('condorcet') != i.get('irv'):
            condorcet_irv += 1
        if i.get('borda') != i.get('irv'):
            borda_irv += 1

    #turn the disagreement integer values into disagreement percentages
    pc_disagreement = str(round(((plurality_condorcet/num_elections) * 100), 2))
    pb_disagreement = str(round(((plurality_borda/num_elections) * 100), 2))
    pi_disagreement = str(round(((plurality_irv/num_elections) * 100), 2))
    cb_disagreement = str(round(((condorcet_borda/num_elections) * 100), 2))
    ci_disagreement = str(round(((condorcet_irv/num_elections) * 100), 2))
    bi_disagreement = str(round(((borda_irv/num_elections) * 100), 2))

    #create array of disagreement percentages and return it, in the format the table creator program accepts
    disagreement_array = [[pc_disagreement, '', ''], [pb_disagreement, cb_disagreement, ''],
                          [pi_disagreement, ci_disagreement, bi_disagreement]]
    return disagreement_array
