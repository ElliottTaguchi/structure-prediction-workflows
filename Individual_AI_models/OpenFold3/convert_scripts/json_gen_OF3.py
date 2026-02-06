import requests
import os
import pandas as pd
import json



def json_gen(of3_input_path, target_fasta="", binder_fasta=""):
    """
    Function to generate A single JSON file for binder and target pairs for OpenFold3 from FASTA files.
    Args:
        of3_input_path (str): Path to save the generated JSON file.
        target_fasta (str): Path to the FASTA file of the target protein.
        binder_fasta (str): Path to the FASTA file of the binder proteins.
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
            else:
                sequences[binder_name] += line.strip()
    #-------- json file generation for of3 input --------#
    all_queries = {"queries": {}}
    for binder_name, binder_seq in sequences.items():
        chain_id_binder = ["A"]
        chain_id_target = ["B"]

        msa_binder = [f"/home/gzs260/OpenFold3/alignments/{binder_name}/"] # update with correct path to MSA directories for binders
        msa_target = ["/home/gzs260/OpenFold3/alignments/EGFR/"] # update with correct path to MSA directory for target

        dict_binder = {"molecule_type": "protein", "chain_ids": chain_id_binder, "sequence": binder_seq, "main_msa_file_paths": msa_binder}

        dict_target = {"molecule_type": "protein", "chain_ids": chain_id_target, "sequence": seq_target, "main_msa_file_paths": msa_target}

        query_name = f"{binder_name}"

        all_queries["queries"][query_name] = {"chains": [dict_binder, dict_target],
                                              "use_msas": "true",
                                              "use_paired_msas": "false",
                                              "use_main_msas": "true"}

        #-------- Write one file --------#
        path_file = os.path.join(of3_input_path, "all_queries.json")
        with open(path_file, "w") as f:
           json.dump(all_queries, f, indent=4)


json_gen(of3_input_path="") # update with correct path to save the generated JSON file
