import json
import os
import glob

"""
Convert JSON files containing protein sequences into A3M MSA files for OpenFold. Creates dummy MSA files.
"""


input_folder = "./json_files/adaptyvbio2_Protenix/"
a3m_output_base = "./a3m_files/openfold/"

for json_file in glob.glob(os.path.join(input_folder, "*.json")):
    with open(json_file, "r") as f:
        data = json.load(f)

    sequence = data["sequences"][0]["proteinChain"]["sequence"]

    binder_name = os.path.basename(json_file).replace(".json", "")
    binder_name = binder_name.replace(".", "_")

    binder_folder = os.path.join(a3m_output_base, binder_name)
    os.makedirs(binder_folder, exist_ok=True)
    output_path = os.path.join(binder_folder, "bfd_uniclust_hits.a3m")

    msa_content = f">query\n{sequence}\n"
    with open(output_path, "w") as f:
        f.write(msa_content)

