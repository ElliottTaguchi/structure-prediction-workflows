from pathlib import Path

"""
Convert a fasta file to an A3M MSA file for OpenFold. Creates a dummy MSA file.
"""

input_dir = Path("./FASTA_files/individual_fasta_v2")
output_dir = Path("./a3m_files/alignments_openfold_new/")

for fasta_file in input_dir.glob("*.fasta"):
    with fasta_file.open() as f:
        lines = f.read().splitlines()
    
    # Extract ID from FASTA header
    if not lines or not lines[0].startswith(">"):
        raise ValueError(f"{fasta_file} is not a valid FASTA file")
    
    fasta_id = lines[0][1:].strip()
    sequence = "\n".join(lines[1:])

    protein_dir = output_dir / fasta_id
    protein_dir.mkdir(exist_ok=True)

    a3m_path = protein_dir / "bfd_uniclust_hits.a3m"
    with a3m_path.open("w") as out:
        out.write(f">{fasta_id}\n")
        out.write(sequence + "\n")

    print(f"Created {a3m_path}")

