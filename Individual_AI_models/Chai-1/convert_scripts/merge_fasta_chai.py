from pathlib import Path
from Bio import SeqIO

"""
Generate merged fasta files for Chai-1, combining binder and target sequences. Done from FASTA files.
"""

binders_dir = Path("") # Specify the directory containing binder FASTA files
target_fasta = Path("") # Specify the target FASTA file
output_dir = Path("") # Specify the output directory

output_dir.mkdir(exist_ok=True, )

target_record = SeqIO.read(target_fasta, "fasta")

target_record.id = f"protein|{target_record.id}"
target_record.description = ""

for binder_file in binders_dir.glob("*.fasta"):
    binder_record = SeqIO.read(binder_file, "fasta")
    binder_record.id = f"protein|{binder_record.id}"
    binder_record.description = ""

    output_file = output_dir / binder_file.name

    SeqIO.write(
        [binder_record, target_record],
        output_file,
        "fasta"
    )
