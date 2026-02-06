from Bio import SeqIO
import os

def split_fasta_biopython(input_fasta: str, individual_fasta_prot: str):
    """
    Splits a multi-sequence FASTA file into individual FASTA files using Biopython.

    Parameters:
    input_fasta (str): Path to the input multi-sequence FASTA file.
    output_dir (str): Directory where individual FASTA files will be saved.
    """
    os.makedirs(individual_fasta_prot, exist_ok=True)
    for record in SeqIO.parse(input_fasta, "fasta"):
        out_path = os.path.join(individual_fasta_prot, f"{record.id}.fasta")
        SeqIO.write(record, out_path, "fasta")

if __name__ == "__main__":
    input_fasta = "./FASTA_files/contest_2_round_2_sequences_v3.fasta"
    individual_fasta_prot = "./FASTA_files/individual_fasta_v3"
    split_fasta_biopython(input_fasta, individual_fasta_prot)

