import requests
import os
import pandas as pd
import json

#af3_input_path="./json_files/af3_input_files/"
#os.makedirs(af3_input_path, exist_ok=True)

def json_gen(HF3_input_path, target_fasta="", binder_fasta=""): # specifify target fasta containing one sequence and binder fasta containing multiple sequences
    """
    Function to generate json files for binder and target pairs for HelixFold from FASTA files, with one target and several binders.
    Parameters:
    HF3_input_path (str): Directory path to save generated JSON files.
    target_fasta (str): Path to the target FASTA file.
    binder_fasta (str): Path to the binder FASTA file containing multiple sequences.
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
        dict_binder = {"type": "protein", "sequence": binder_seq, "count": 1}
        dict_target = {"type": "protein", "sequence": seq_target, "count": 1}
        dict_RC["entities"]=[dict_binder, dict_target]
        path_file = os.path.join(HF3_input_path, f"{binder_name}.json")
        with open(path_file, "w") as f:
           json.dump(dict_RC, f, indent=4)


json_gen(HF3_input_path="") # specify the desired directory path to save the generated JSON files