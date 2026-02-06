from Bio import SeqIO
import yaml
import os

def fasta_to_yaml(binders_fasta, target_fasta, output_dir):
    """
    Merges a fasta file of binders and a fasta file of a single target (the same for all binders) into individual YAML files for each prediction pair. Made to take a precomputed msa for the target and none for the binders.
    Parameters:
    binders_fasta (str): Path to the FASTA file containing multiple binder sequences.
    target_fasta (str): Path to the FASTA file containing a single target sequence.
    output_dir (str): Directory to save the generated YAML files.
    """
    binders = list(SeqIO.parse(binders_fasta, "fasta"))

    target = next(SeqIO.parse(target_fasta, "fasta"))

    os.makedirs(output_dir, exist_ok=True)

    entity = "protein"

    for binder in binders:
        yaml_data = {
            "sequences": [
                {
                entity: {
                    "id": "A",
                    "sequence": str(binder.seq),
                    "msa": "empty"
                    }
                },
                {
                entity: {
                    "id": "B",
                    "sequence": str(target.seq),
                    "msa": "./precomputed_msa/target/egfr_msa_AF3_generated.a3m" ### Change this path as needed
                    }
                }
            ]
        }
        
        out_path = os.path.join(output_dir, f"{binder.id}.yaml")
    
        with open(out_path, 'w') as f:
            yaml.dump(yaml_data, f, sort_keys=False)

    print(f"Generated YAML file with {len(binders)} binder entries: {output_dir}")

if __name__ == "__main__":
    binders_fasta = "" # Specify the path to the FASTA file containing multiple binder sequences
    target_fasta = "" # Specify the path to the FASTA file containing a single target sequence
    output_dir = "" # Specify the output directory
    fasta_to_yaml(binders_fasta, target_fasta, output_dir)