import requests
import os
import pandas as pd
import json


def json_gen(Protenix_input_path, target_fasta="", binder_fasta=""): # update with correct default paths if needed
    """
    Function to generate json files for binder and target pairs for Protenix from FASTA files.
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

    #-------- new json file generation for protenix input --------#
    for binder_name, binder_seq in sequences.items():
        binder_msa_dir = f"/home/postyr/Protenix/precomputed_msa/binder/{binder_name}" # update with correct path to MSA directories for binders
        binder_entry = {
                    "proteinChain": {
                        "sequence": binder_seq,
                        "count": 1,
                        "msa": {
                            "precomputed_msa_dir": binder_msa_dir,
                            "pairing_db": "uniref100"
                        }
                    }
                }
        
        target_entry = {
            "proteinChain": {
                "sequence": seq_target,
                "count": 1,
                        "msa": {
                            "precomputed_msa_dir": "/home/postyr/Protenix/precomputed_msa/target", # update with correct path to MSA directory for target
                            "pairing_db": "uniref100"
                        }                
                    }   
                }
        combined_obj = {
            "sequences": [binder_entry, target_entry],
            "name": binder_name + "_EGFR"
        }

        path_file = os.path.join(Protenix_input_path, f"{binder_name}.json")
        with open(path_file, "w") as f:
            json.dump([combined_obj], f, indent=4)

json_gen(Protenix_input_path="") # update with correct path to save the generated JSON files