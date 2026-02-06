
import requests
import os
import pandas as pd
import json

#af3_input_path="./json_files/af3_input_files/"
#os.makedirs(af3_input_path, exist_ok=True)

def json_gen(af3_input_path, target_fasta="", binder_fasta=""):
    """
    Function to generate json files for binder and target pairs for AF3 from FASTA files.
    Satisfies the criteria for AlphaFold3 input JSON structure.
    1 target sequence from target_fasta and multiple binder sequences from binder_fasta.
    Parameters:
    af3_input_path (str): Directory path to save generated JSON files.
    target_fasta (str): Path to the target FASTA file.
    binder_fasta (str): Path to the binder FASTA file.
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
        dict_RC["modelSeeds"] = [0]
        chain_id_binder = "A"
        chain_id_target = "B"
        dict_binder = {"protein":{"id":chain_id_binder, "sequence": binder_seq, "unpairedMsa": "", "pairedMsa": ""}}
        dict_target = {"protein": {"id": chain_id_target, "sequence": seq_target, "unpairedMsaPath": "", "pairedMsa": ""}} # set unpairedMsaPath for the target to the desired MSA file path
        dict_RC["sequences"]=[dict_binder, dict_target ]
        dict_RC["dialect"] = "alphafold3"
        dict_RC["version"] = 1
        path_file = os.path.join(af3_input_path, f"{binder_name}.json")
        with open(path_file, "w") as f:
           json.dump(dict_RC, f, indent=4)


json_gen(af3_input_path="./json_files/AF3_with_MSA/")