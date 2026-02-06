from Bio import SeqIO
import yaml
import os

def fasta_to_yaml(target_fasta, output_dir="yaml_files/"):
    """
    Creates a YAML file for a single target protein from a fasta file.
    """

    target = next(SeqIO.parse(target_fasta, "fasta"))

    os.makedirs(output_dir, exist_ok=True)

    yaml_data = {
        "sequences": [
            {
                "protein": {
                    "id": "EGFR",
                    "sequence": str(target.seq),
                }
            }
        ]
    }
        
    out_path = os.path.join(output_dir, "EGFR.yaml")
    
    with open(out_path, 'w') as f:
        yaml.dump(yaml_data, f, sort_keys=False, default_flow_style=False, indent=2)


if __name__ == "__main__":
    target_fasta = "./FASTA_files/EGFR_target_contest2.fasta"
    fasta_to_yaml(target_fasta)