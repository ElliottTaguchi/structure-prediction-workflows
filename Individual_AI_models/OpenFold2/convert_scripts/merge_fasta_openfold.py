from pathlib import Path
from Bio import SeqIO

"""
Generate merged fasta files for OpenFold2, combining binder and target sequences. Done from FASTA files.
"""


binders_dir = Path("") # Specify the directory containing binder FASTA files
target_fasta = Path("") # Specify the target FASTA file
output_dir = Path("") # Specify the output directory

output_dir.mkdir(exist_ok=True)

target_record = SeqIO.read(target_fasta, "fasta")

# Replace dots in target header
target_record.id = target_record.id.replace(".", "_")
target_record.description = ""

for binder_file in binders_dir.glob("*.fasta"):
    binder_record = SeqIO.read(binder_file, "fasta")
    binder_record.id = binder_record.id.replace(".", "_")
    binder_record.description = ""

    output_filename = binder_file.stem.replace(".", "_") + ".fasta"
    output_file = output_dir / output_filename

    SeqIO.write(
        [binder_record, target_record],
        output_file,
        "fasta"
    )
