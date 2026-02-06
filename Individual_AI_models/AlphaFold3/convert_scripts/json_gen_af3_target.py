import requests
import os
import pandas as pd
import json

#af3_input_path="./json_files/af3_input_files/"
#os.makedirs(af3_input_path, exist_ok=True)

def json_gen(af3_input_path, target_fasta=""):
    """
    Function to generate a json file for a single target for AF3 from a FASTA file.
    Parameters:
    af3_input_path (str): Directory path to save generated JSON file.
    target_fasta (str): Path to the target FASTA file.
    """
    seq_target = ""

    with open(target_fasta, "r") as f:
        txt = f.readlines()
        for line in txt:
            if line.startswith(">"):
                continue
            else:
                seq_target += line.strip()

    #-------- json file generation for af3 input --------#
    for seq_target in [seq_target]:
        dict_RC = {}
        dict_RC["name"]= "EGFR" # this is the one for the bider ids
        dict_RC["modelSeeds"] = [0]
        chain_id_target = "A"
        dict_target = {"protein": {"id": chain_id_target, "sequence": seq_target}}
        dict_RC["sequences"]=[dict_target]
        dict_RC["dialect"] = "alphafold3"
        dict_RC["version"] = 1
        path_file = os.path.join(af3_input_path, "") # specify the desired name for the output JSON file
        with open(path_file, "w") as f:
           json.dump(dict_RC, f, indent=4)


json_gen(af3_input_path="") # specify the desired directory path to save the generated JSON file