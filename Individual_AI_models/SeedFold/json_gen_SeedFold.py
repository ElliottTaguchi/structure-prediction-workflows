import requests
import os
import pandas as pd
import json

#af3_input_path="./json_files/af3_input_files/"
#os.makedirs(af3_input_path, exist_ok=True)

def json_gen(SF_input_path, target_fasta="/Users/elliotttaguchidickinson/Desktop/DeNovoProteinHal/contest_2/fasta_files/EGFR.fasta", binder_fasta="/Users/elliotttaguchidickinson/Desktop/DeNovoProteinHal/contest_2/fasta_files/all_binders_ID-.fasta"):
    """
    A function to generate the desired JSON files for SeedFold from Fasta files.
    """
    seq_target = ""

    with open(target_fasta, "r") as f:
        txt = f.readlines()
        for line in txt:
            if line.startswith(">"):
                continue
            else:
                seq_target += line.strip()

    sequences = {} # dictionary to hold all sequences

    with open(binder_fasta, "r") as f:
        txt = f.readlines()
        for line in txt:
            if line.startswith(">"):
                binder_name = line.replace(">", "").strip()
                sequences[binder_name] = ""
                continue
            else:
                sequences[binder_name] += line.strip()
    #-------- json file generation for af3 input --------#
    for binder_name, binder_seq in sequences.items():
        dict_RC = {}
        dict_RC["name"]= f"{binder_name}" # this is the one for the bider ids
        chain_id_binder = "A"
        chain_id_target = "B"
        dict_binder = {"entity": "protein", "copies": 1, "sequence": binder_seq}
        dict_target = {"entity": "protein", "copies": 1, "sequence": seq_target}
        dict_RC=[dict_binder, dict_target]
        path_file = os.path.join(SF_input_path, f"{binder_name}.json")
        with open(path_file, "w") as f:
           json.dump(dict_RC, f, indent=4)


json_gen(SF_input_path="/Users/elliotttaguchidickinson/Desktop/DeNovoProteinHal/contest_2/json_files/for_albert")